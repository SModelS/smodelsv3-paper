#!/usr/bin/env python3

from __future__ import print_function
import logging, shutil
import time,datetime

import sys,os,glob,copy
import pandas as pd
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


def getBRratio(banner_file):

    # quarks masses
    MU = 0.00255
    MC = 1.27
    MT = 172
    MD = 0.00504
    MS = 0.101
    MB = 4.7

    # couplings
    gAq = 0.0
    gAu11 = gAq
    gAu22 = gAq
    gAu33 = gAq
    gAd11 = gAq
    gAd22 = gAq
    gAd33 = gAq

    gVq = 0.25
    gVu11 = gVq
    gVu22 = gVq
    gVu33 = gVq
    gVd11 = gVq
    gVd22 = gVq
    gVd33 = gVq

    gAXd = 0.0
    gVXd = 1.0


    gZp = 1.0
    gqA = 0.0

    for b in [banner_file]:
        xtree = ET.parse(b)
        xroot = xtree.getroot()
        slha = xroot.find('header').find('slha').text
        pars = pyslha.readSLHA(slha)
        # bsm parameters
        mz = pars.blocks['MASS'][9900032]
        mx = pars.blocks['MASS'][9000006]
        gq = pars.blocks['ZPRIME'][2]
        gx = pars.blocks['ZPRIME'][1]
     
    ### Simplified model BR
    if (2*mx < mz):
        Y1bb = (mz**2*(12*gAd33**2*mz**2 + 12*gVd33**2*mz**2))/(48.*np.pi*abs(mz)**3)
        Y1cc = (mz**2*(12*gAu22**2*mz**2 + 12*gVu22**2*mz**2))/(48.*np.pi*abs(mz)**3)
        Y1dd = (mz**2*(12*gAd11**2*mz**2 + 12*gVd11**2*mz**2))/(48.*np.pi*abs(mz)**3)
        Y1ss = (mz**2*(12*gAd22**2*mz**2 + 12*gVd22**2*mz**2))/(48.*np.pi*abs(mz)**3)
        Y1tt = ((-48*gAu33**2*MT**2 + 24*gVu33**2*MT**2 + 12*gAu33**2*mz**2 + 12*gVu33**2*mz**2)*np.sqrt(-4*MT**2*mz**2 + mz**4))/(48.*np.pi*abs(mz)**3)
        Y1uu = (mz**2*(12*gAu11**2*mz**2 + 12*gVu11**2*mz**2))/(48.*np.pi*abs(mz)**3)
        Y1xdxd = ((-16*gAXd**2*mx**2 + 8*gVXd**2*mx**2 + 4*gAXd**2*mz**2 + 4*gVXd**2*mz**2)*np.sqrt(-4*mx**2*mz**2 + mz**4))/(48.*np.pi*abs(mz)**3)
    
        # Total width
        
        GammaY1 = Y1bb + Y1cc + Y1dd + Y1ss + Y1tt + Y1uu + Y1xdxd
        
        # BR(y1 to xd xd~)
        
        brSimp = Y1xdxd / GammaY1

        ### 2MDM BR
        
        gqR = (-gqA + gq)
        gqL = (gqA + gq)
        ZPtt = ((-6*gqL**2*gZp**2*MT**2 + 36*gqL*gqR*gZp**2*MT**2 - 6*gqR**2*gZp**2*MT**2 
                             + 6*gqL**2*gZp**2*mz**2 + 6*gqR**2*gZp**2*mz**2)
                            *np.sqrt(-4*MT**2*mz**2 + mz**4))/(48.*np.pi*abs(mz)**3)   
        ZPuu = (mz**2*(6*gqL**2*gZp**2*mz**2 + 6*gqR**2*gZp**2*mz**2))/(48.*np.pi*abs(mz)**3)
        ZPcc = (mz**2*(6*gqL**2*gZp**2*mz**2 + 6*gqR**2*gZp**2*mz**2))/(48.*np.pi*abs(mz)**3)
        ZPdd = (mz**2*(6*gqL**2*gZp**2*mz**2 + 6*gqR**2*gZp**2*mz**2))/(48.*np.pi*abs(mz)**3)
        ZPss = (mz**2*(6*gqL**2*gZp**2*mz**2 + 6*gqR**2*gZp**2*mz**2))/(48.*np.pi*abs(mz)**3)
        ZPbb = (mz**2*(6*gqL**2*gZp**2*mz**2 + 6*gqR**2*gZp**2*mz**2))/(48.*np.pi*abs(mz)**3)
        ZPchichi = ((-16*gx**2*mx**2 + 4*gx**2*mz**2)*np.sqrt(-4*mx**2*mz**2 + mz**4))/(96.*np.pi*abs(mz)**3)
        GammaZP = ZPuu + ZPcc + ZPtt + ZPdd + ZPss + ZPbb + ZPchichi
        br2mdm = ZPchichi / GammaZP

        brRatio = brSimp/br2mdm
    
    else:
        brRatio = 1.0


    # BRdata = pd.read_pickle('data/BRdata-models.pcl')
    # # filterBR_ZPchichi = ZPchichi / GammaZP

    # BRdata = BRdata[(BRdata['$m_{med}$'] == mz) & (BRdata['$m_{chi}$'] == mx)]
    # brSimp = BRdata['$BR(med>\chi\chi)$'][(BRdata['Model'] == 'DMsimp')]
    # br2mdm = BRdata['$BR(med>\chi\chi)$'][(BRdata['Model'] == '2MDM') & (BRdata['Mediator'] == 'spin-1') & (BRdata['$g_{q}$'] == gq) & (BRdata['$g_{\chi}$'] == gx)]

    # brRatio = float(brSimp)/float(br2mdm)

    return brRatio


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
        if 9900032 in finalStates: 
            k = getBRratio(banner_file)
        elif 9900026 in finalStates:  
            k = 1.0
        print(k)

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
                print(finalStates)
                xsec = xsec*k
                slhaF.write("  0  0  0  0  0  303600  %1.4e madgraph 3.5.1 \n" %xsec) 
                slhaF.write('\n\n')
    slhaF.close()
                
    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))