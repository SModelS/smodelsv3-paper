#!/usr/bin/env python3

from __future__ import print_function
import logging, shutil
import time,datetime

import sys,os,glob,copy
import numpy as np
import pyslha
import xml.etree.ElementTree as ET

mg5Folder = os.path.abspath('../MG5')
sys.path.append(mg5Folder)
from madgraph.various.banner import Banner

# Function for obtaining the slha data (param card) given banner file
def GetParams(banner_file):
    banner = Banner()
    banner.read_banner(banner_file)
    slhaData = banner['slha']

    for b in [banner_file]:
        xtree = ET.parse(b)
        xroot = xtree.getroot()
        slha = xroot.find('header').find('slha').text
        pars = pyslha.readSLHA(slha)
        msd = pars.blocks['BLINPUTS'][2]

    for l in slhaData.split('\n'):
        if not ' sd ' in l: continue
        oldline = l
        line = l.split()
        line[1] = str(msd)
        fixline = ' '.join(line)

    slhaData = slhaData.replace(oldline, '      '+fixline)
    
    return slhaData

# Function that obtains final states, cross section and x-section error for slha xsection block
def GetXsection(banner_file):
    # particles of 2mdm model
    pdg_zp = 9900032
    pdg_sd = 9900026
    pdg_chi = 9000006
    
    banner = Banner()
    banner.read_banner(banner_file)
    finalStates = []
    
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
            finalStates.append([pdg_chi, pdg_chi])
            
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

if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser( description=
            "Simple script to obtain slha file from given banners." )
    ap.add_argument('-f', '--inputFile', required=True, nargs='+', help='banner files.'
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
    if outputFile is None:
        outputFile = inputFile[0].replace('_banner.txt', '.slha')

    t0 = time.time()

    # Get parameters (only for first banner)
    slhaData = GetParams(inputFile[0])

    slhaF = open(outputFile, 'w')
    slhaF.write(slhaData)
    slhaF.write('\n\n')

    for banner_file in inputFile:
        pdgInitial, finalStates, processXsecs, sqrts = GetXsection(banner_file)
        print('Initial states (pdg): ',pdgInitial,', final state(s) (pdg): ',finalStates)
        
        for procID in processXsecs:
            if (procID == 1) or (procID == 0):
                xsec = processXsecs[procID]['xsec (pb)']
                xsecErr = processXsecs[procID]['xsecErr (pb)']
                print('Cross-section (pb) = ',xsec,' +/- ',xsecErr)
                comment = "# xsec unit: pb xsec error: %1.3e" %(xsecErr)
                xsecLine = "\nXSECTION %1.3e " %(sqrts)
                xsecLine += " ".join([str(pdg) for pdg in pdgInitial])
                xsecLine += " %i " %len(finalStates)
                xsecLine += " ".join([str(pdg) for pdg in finalStates])
                slhaF.write(xsecLine+' '+comment+' \n')        
                slhaF.write("  0  0  0  0  0  303600  %1.4e madgraph 3.5.1 \n" %xsec) 
                slhaF.write('\n\n')
    slhaF.close()
                
    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))