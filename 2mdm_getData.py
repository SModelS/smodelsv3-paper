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

    for evts in [events]:
        modelDict['Events'] = nevts
        for event in evts:
            weight = event.eventinfo.weight/nevts
            totalweight += weight

    modelDict['x-sec (pb)'] = totalweight

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
