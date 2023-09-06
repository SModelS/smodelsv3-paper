#!/usr/bin/env python3

import os, sys, glob, copy
from pyexpat import model
import numpy as np 
import pandas as pd 
import pyslha
import pylhe
import xml.etree.ElementTree as ET 

def getModelDict(inputFile):
    
    modelDict = {}

    lheFile = sorted(glob.glob(os.path.dirname(inputFile[0])+'/*.lhe.gz'), key=os.path.getmtime, reverse=True)[0]

    banner = inputFile

    if len(banner) == 0:
        print('Banner not found for %s' %inputFile[0])
        return None

    elif len(banner) > 1:
        print('\n%i banner files found for %s.' %(len(banner), os.path.dirname(inputFile[0])))
        matches = [set(os.path.basename(inputFile[0])).intersection(set(os.path.basename(b))) for b in banner]
        banner = banner[np.argmax(matches)]
        print('Using banner %s' %banner)

    else:
        banner = banner[0]

    xtree = ET.parse(banner)
    xroot = xtree.getroot()
    slha = xroot.find('header').find('slha').text
    pars = pyslha.readSLHA(slha)

    if 9900032 in pars.blocks['MASS']:
        process = 'pp->zp'
        modelDict['process'] = process
        mMed = pars.blocks['MASS'][9900032] # Z prime mass
        mH2 = pars.blocks['BLINPUTS'][2] # dark Higgs mass
        

    if 54 in pars.blocks['MASS']:
        process = 'pp->y0'
        modelDict['process'] = process
        mMed = pars.blocks['MASS'][54]  # modified Y0 mass
        

    if process == 'pp->zp':
        mChi = pars.blocks['MASS'][9000006] # DM mass
        sTheta = pars.blocks['BLINPUTS'][3] # sin theta
        gchi = pars.blocks['ZPRIME'][1] # coupling of mediators to DM
        gq = pars.blocks['ZPRIME'][2] # coupling of mediators to SM
        gammaZp = pars.decays[9900032].totalwidth # zp total width
        gammaS = pars.decays[9900026].totalwidth # s total width

        modelDict['$m_{med}$'] = mMed
        modelDict['$m_{s}$'] = mH2
        modelDict['$\Gamma_{zp}$'] = gammaZp



    if process == 'pp->y0':
        mChi = pars.blocks['MASS'][52] # DM mass
        sTheta = pars.blocks['DMINPUTS'][10] # sin theta
        gchi = pars.blocks['DMINPUTS'][3]
        gq = pars.blocks['DMINPUTS'][6]
        gammaS = pars.decays[54].totalwidth

        modelDict['$m_{med}$'] = mMed

    modelDict['$\Gamma_{s}$'] = gammaS
    modelDict['$m_{\chi}$'] = mChi
    modelDict['$g_{\chi}$'] = gchi
    modelDict['$g_{q}$'] = gq
    modelDict['$\sin\\theta$'] = sTheta

    with pylhe._extract_fileobj(lheFile) as fileobj:
        nevts = sum(element.tag == "event" for event, element in ET.iterparse(fileobj, events=["end"]))

    events = pylhe.read_lhe_with_attributes(lheFile)

    totalweight = 0
    totalweight_cut = 0

    ## jets
    pTj1min = 100.
    pTjmin = 20.
    etamax = 2.4
    ## MET
    minMET = 250.



    for evts in [events]:
        modelDict['Events'] = nevts
        for event in evts:

            particles = event.particles

            jets = [p for p in particles if abs(p.id) in [1,2,3,4,5,21] and p.status == 1]
            dm = [p for p in particles if abs(p.id) in [9000006, 52] and p.status == 1]
            med = [p for p in particles if abs(p.id) in [9900032, 9900026] and p.status == 1]

            if len(med) != 1:
                continue

            weight = event.eventinfo.weight/nevts

            if weight < 0:
                continue

            totalweight += weight

            # Filter jets
            jetList = []
            for j in jets:
                pT = np.sqrt(j.px**2+j.py**2)
                p = np.sqrt(j.px**2+j.py**2+j.pz**2)
                pL = j.pz
                eta = 0.5*np.log((p+pL)/(p-pL))
            
                if pT < pTjmin:
                    continue
                if np.abs(eta) > etamax:
                    continue
                jetList.append(j)
            jetList = sorted(jetList, key = lambda j: np.sqrt(j.px**2+j.py**2), reverse=True) 

            # Compute MET
            # MET = np.sqrt((dm[0].px+dm[1].px)**2 + (dm[0].py+dm[1].py)**2)
            MET = np.sqrt((med[0].px)**2 + (med[0].py)**2)

            if len(jetList) == 0:
                continue

            pT1 = np.sqrt(jetList[0].px**2+jetList[0].py**2)
            if MET < minMET:
                continue
            if pT1 < pTj1min:
                continue

            totalweight_cut += weight

    modelDict['x-sec (pb)'] = totalweight
    modelDict['x-sec pT-250 (pb)'] = totalweight_cut

    print('Total cross section = %1.4f (pb)' %totalweight)

    return modelDict

if __name__ == '__main__':

    import argparse

    ap = argparse.ArgumentParser(description = 'Obtain the cross section and widths for a given banner file.')
    ap.add_argument('-f', '--inputFile', required=True, nargs='+', help='banner file')
    ap.add_argument('-o', '--outputFile', required = False, help = 'output file.'
                     + 'If not defined, will use the name of the input file.', default = None)

    args = ap.parse_args()
    inputFile = args.inputFile
    outputFile = args.outputFile
    if outputFile is None:
        outputFile = inputFile[0].replace('banner.txt', 'data.pcl')
        # outputFile = outputFile.replace(/[\[\]']+/g,'')

    if os.path.splitext(outputFile)[1] != '.pcl':
        outputFile = os.path.splitext(outputFile)[0]

    modelDict = getModelDict(inputFile)

    df = pd.DataFrame.from_dict(modelDict, orient = 'index').T

    print('Saving to', outputFile)
    df.to_pickle(outputFile)
