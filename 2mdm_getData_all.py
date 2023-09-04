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

    # Get banner

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

    # Get parameters from model 2mdm

    mZp = pars.blocks['MASS'][9900032] # Z prime mass
    mH1 = pars.blocs['MASS'][9900025] # SM Higgs mass
    mH2 = pars.blocks['BLINPUTS'][2] # dark Higgs mass
    mChi = pars.blocks['MASS'][9000006] # DM mass

    sTheta = pars.blocks['BLINPUTS'][3] # sin theta
    sEpsilon = pars.blocks['BLINPUTS'][4] # sin epsilon

    gchi = pars.blocks['ZPRIME'][1] # coupling of mediators to DM
    gq = pars.blocks['ZPRIME'][2] # coupling of mediators to SM
    g1p = pars.blocks['BLINPUTS'][1] # g1p

    gammaZp = pars.decays[9900032].totalwidth # zp total width
    gammaH2 = pars.decays[9900026].totalwidth # dark Higgs total width



    modelDict['$m_{med}$'] = mZp
    modelDict['$m_{h2}$'] = mH2
    modelDict['$m_{h1}$'] = mH1
    modelDict['$\Gamma_{zp}$'] = gammaZp
    modelDict['$\Gamma_{h2}$'] = gammaH2
    modelDict['$m_{\chi}$'] = mChi
    modelDict['$g_{\chi}$'] = gchi
    modelDict['$g_{q}$'] = gq
    modelDict['$g_{1p}$'] = g1p
    modelDict['$\sin\\theta$'] = sTheta
    modelDict['$\sin\\epsilon$'] = sEpsilon

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
        outputFile = inputFile[0].replace('banner.txt', 'data_all.pcl')
        # outputFile = outputFile.replace(/[\[\]']+/g,'')

    if os.path.splitext(outputFile)[1] != '.pcl':
        outputFile = os.path.splitext(outputFile)[0]

    modelDict = getModelDict(inputFile)

    df = pd.DataFrame.from_dict(modelDict, orient = 'index').T

    print('Saving to', outputFile)
    df.to_pickle(outputFile)
