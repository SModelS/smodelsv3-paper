#!/usr/bin/env python3

from __future__ import print_function
import logging, shutil
import time,datetime

import sys,os,glob,copy
import pyslha
import xml.etree.ElementTree as ET

mg5Folder = os.path.abspath('/Users/ramos/MonoXSMS/MG5/')
sys.path.append(mg5Folder)
from madgraph.various.banner import Banner
import gzip

#def FixParams(slhaData):
#    """
#    Function that fixes the S mediator mass;
#    :param slhaData:  variable that contains relevant parameters for the slha file;
#    :return: the slhaData with fixed S mediator mass.
#    """
##     banner = Banner()
##     banner.read_banner(banner_file)
##     slhaData = banner['slha']
#    
#    pars = pyslha.readSLHA(slhaData)
#    msd = pars.blocks['BLINPUTS'][2]
#    
#    for l in slhaData.split('\n'):
#        if not ' sd ' in l: continue
#        oldline = l
#        line = l.split()
#        line[1] = str(msd)
#        fixline = ' '.join(line)
#    slhaData = slhaData.replace(oldline, '      '+fixline)
#    
#    
#    return slhaData
    

def GetXsection(banner_file):
    """
    Function that obtain relevant info for the .slha file;
    :param banner_file: file that contains info about the MG5 run, being either in the '_banner.txt' or in the '.lhe' format;
    :return: pdg codes for final and initial states, cross-sectios and its error, and center-of-mass energy.
    """
    
    # particles of 2mdm model
    pdg_zp = 9900032
    pdg_sd = 9900026
    pdg_chi = 9000006

    finalStates = []
    
    banner = Banner()
    banner.read_banner(banner_file)
    

    # get final states. If zp (sd) is in proc card, the process considered is p p > zp (p p > sd), otherwise it is p p > chi chi
    for l in banner['mg5proccard'].split('\n'):
        if (not '>' in l) or (not l):
            continue
        if 'j' in l:
            continue
        l = l.strip()
        print(l.replace('generate', 'process'))
        if 'zp' in l:
            finalStates.append(pdg_zp)
        elif 'sd' in l:
            finalStates.append(pdg_sd)
        elif 'chi' in l:
            finalStates = [pdg_chi, pdg_chi]

    # get process information
    info = banner['init'].split('\n')[0].split()
    sqrts = eval(info[2]) + eval(info[3])
    pdgInitial = list(banner.get_pdg_beam())
    processXsecs = {}

    vals, xsec, xsecErr, _, procID = [], [], [], [], []
    for l in banner['init'].split('\n')[1:]:
        if not l.strip() or l.strip()[0] == '<':
            continue
        for x in l.split('\n'):
            vals.append(x.split())

    for v in vals:
        for i in range(len(v)):
            v[i] = eval(v[i])
        xsec.append(v[0])
        xsecErr.append(v[1])
        procID.append(v[3])

    for i in range(len(procID)):
        processXsecs[procID[i]] = {'xsec (pb)' : xsec[i], 'xsecErr (pb)' : xsecErr[i]}

    return pdgInitial, finalStates, processXsecs, sqrts

def GetSLHAname(banner_file):
    """
    Function that obtains the run_tag to name the slha file in the format 'run_*_{run_tag}.slha';
    :param banner_file:  file that contains info about the MG5 run, being either in the '_banner.txt' or in the '.lhe' format;
    :return: the tag of the run.
    """
    
    banner = Banner()
    banner.read_banner(banner_file)
    
    for l in banner['mgruncard'].split('\n'):
        if 'run_tag' not in l: continue
        else:
            run_tag = l.split()
            run_tag = run_tag[0]
            
    return run_tag

if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser( description=
            "Simple script to obtain slha file from given banners." )
    ap.add_argument('-f', '--inputFile', required=True, nargs='+', help='file containing banner information. Can be either in the .txt or in the .lhe format'
                    + 'From the first banner the script will extract the param files and the cross-section.'
                    + 'From the second banner the script will extract only the cross-section information.'
                    + 'Therefore, both banners must contains the same initial parameters (masses, couplings, decays, etc).')
    ap.add_argument('-o', '--outputFile', required = False, help = 'output file.'
                     + 'If not defined, will use the name of the input file.', default = None)
    ap.add_argument('-v', '--verbose', default='error',
            help='verbose level (debug, info, warning or error). Default is error')

    args = ap.parse_args()
    inputFile = args.inputFile
    outputFile = args.outputFile

    t0 = time.time()

    print('\n#######################\n')

    print('Creating SLHA file for file(s): ')
    for file in inputFile:
        print(file)
        
    print('\n')

    # Get slha data and fix S mass

    if '.lhe' in inputFile[0]:
        with gzip.open(inputFile[0], 'rt') as f:
            run_tag = GetSLHAname(f)

        with gzip.open(inputFile[0], 'rt') as f:
            banner = Banner()
            banner.read_banner(f)
            slhaData = banner['slha']
#            slhaData = FixParams(slhaData)
            
    elif '.txt' in inputFile[0]:
        run_tag = GetSLHAname(inputFile[0])
        banner = Banner()
        banner.read_banner(inputFile[0])
        slhaData = banner['slha']
#        slhaData = FixParams(slhaData)

    if outputFile is None:

        run_number = os.path.dirname(inputFile[0]).split('/')[-1]
        outputFile = os.path.dirname(inputFile[0])+'/'+run_number+'_'+run_tag+'.slha'
    slhaF = open(outputFile, 'w')
    slhaF.write(slhaData)
    slhaF.write('\n\n')

    print('Saving data for process(es):\n')
    
    for file in inputFile:
        if '.lhe' in file:
            with gzip.open(file, 'rt') as f:
                pdgInitial, finalStates, processXsecs, sqrts = GetXsection(f)
                print('Initial states (pdg): ',pdgInitial,', final state(s) (pdg): ',finalStates)

                for procID in processXsecs:
                    if (procID == 1) or (procID == 0):
                        xsec = processXsecs[procID]['xsec (pb)']
                        xsecErr = processXsecs[procID]['xsecErr (pb)']
                        print('Cross-section (pb) = ',xsec,' +/- ',xsecErr,'\n')
                        comment = "# xsec unit: pb xsec error: %1.3e" %(xsecErr)
                        xsecLine = "\nXSECTION %1.3e " %(sqrts)
                        xsecLine += " ".join([str(pdg) for pdg in pdgInitial])
                        xsecLine += " %i " %len(finalStates)
                        xsecLine += " ".join([str(pdg) for pdg in finalStates])
                        slhaF.write(xsecLine+' '+comment+' \n')        
                        slhaF.write("  0  0  0  0  0  303600  %1.4e madgraph 3.5.1 \n" %xsec) 
                        slhaF.write('\n\n')
                        
        elif '.txt' in inputFile:
            pdgInitial, finalStates, processXsecs, sqrts = GetXsection(file)
            print('Initial states (pdg): ',pdgInitial,', final state(s) (pdg): ',finalStates)

            for procID in processXsecs:
                if (procID == 1) or (procID == 0):
                    xsec = processXsecs[procID]['xsec (pb)']
                    xsecErr = processXsecs[procID]['xsecErr (pb)']
                    print('Cross-section (pb) = ',xsec,' +/- ',xsecErr,'\n')
                    comment = "# xsec unit: pb xsec error: %1.3e" %(xsecErr)
                    xsecLine = "\nXSECTION %1.3e " %(sqrts)
                    xsecLine += " ".join([str(pdg) for pdg in pdgInitial])
                    xsecLine += " %i " %len(finalStates)
                    xsecLine += " ".join([str(pdg) for pdg in finalStates])
                    slhaF.write(xsecLine+' '+comment+' \n')        
                    slhaF.write("  0  0  0  0  0  303600  %1.4e madgraph 3.5.3 \n" %xsec) 
                    slhaF.write('\n\n')

    slhaF.close()

    print('Saving slha file to:', outputFile)
    print('\n##############################\n')
                
    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))
