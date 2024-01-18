import sys, os
from configParserWrapper import ConfigParserExt
from scipy import interpolate
import pandas as pd
import numpy as np
import logging,shutil
import subprocess
import tempfile
import time,datetime
import itertools
import multiprocessing
from collections import OrderedDict

def GetProcess(finalState, initialStates=['p','p']):
    '''
    Function that obtains the process of interest and returns as string with the process

    :param finalState: list of final string or PDG (e.g. ['zp'])
    :param initalStates: list of inital state string, default is ['p','p']

    :return: Process string
    '''
    pass

def GetXSection(Mmed=2000, pid=9900032, s=13):
    '''
    Function that obtains the cross sections from interpolation given the input mass for the 2MDM model

    :param Mmed: mediator particle mass (in GeV)
    :param pid: mediator id 
    :param s: center of mass energy, default is 13 TeV

    :return: mediator production cross-section (in pb)
    '''

    dataScan = pd.read_pickle('./data/smodels-results/results.pcl')

    if s == 13:
        xsecLabel = 'xsec13TeV(fb).'+str(pid)
    elif s == 8:
        xsecLabel = 'xsec8TeV(fb).'+str(pid)
    xsecScan = dataScan[['mass.'+str(pid), xsecLabel]]
    xsecFunction = interpolate.interp1d(xsecScan['mass.'+str(pid)], xsecScan[xsecLabel])

    xsecNew = int(xsecFunction(Mmed))/1000

    return xsecNew

def GetBR(MSd=1000, MZp=2000, Mchi=65, gqV=0.25, gchi=1.6, Sa=0.25, ychi=1.0):
    '''
    Function that obtains the branching ratio for given parameters for the 2MDM model

    :param MZp: spin-1 mediator particle mass in GeV
    :param MSd: spin-0 mediator particle mass in GeV
    :param pid: mediator id 
    :param Mchi: dark matter mass in GeV
    :param gq: mediator coupling to quarks
    :param gq: mediator coupling to dm

    :return: dictionary with possible branching ratios and widths
    '''
    ## define constants

    # mass for quarks
    MU = 0
    MC = 0
    MT = 172
    MD = 0
    MS = 0
    MB = 0

    # tau lepton mass
    MTA = 1.777

    # gauge bosons masses
    MW = 79.824
    MZ = 91.1876

    # higgs boson mass
    MH = 125.0

    aEWM1 = 127.9
    aEW = 1/aEWM1
    ee = 2*np.sqrt(aEW)*np.sqrt(np.pi)

    sw2 = 1 - MW**2/MZ**2
    sw = np.sqrt(sw2)
    cw = np.sqrt(1 - sw2)

    # vevs
    vev = (2*MW*sw)/ee
    gchi = 1.0
    vev2 = MZp/(2*gchi)

    # couplings
    yt = np.sqrt(2)*MT/vev
    ytau = np.sqrt(2)*MTA/vev
    gqA = 0.0
    gZp = 1.0

    ### spin-1 mediator ###
    gqL = (gqA + gqA)
    gqR = (-gqA + gqA)

    # Zp to t 
    if MZp < 2*MT:
        ZPtt = 0
    else:
        ZPtt = ((-6 * gqL**2 * gZp**2 *MT**2 + 36 * gqL * gqR * gZp**2 * MT**2 - 6 * gqR**2 *gZp**2 * MT**2 
                 + 6 * gqL**2 * gZp**2 * MZp**2 + 6 * gqR**2 * gZp**2 * MZp**2)
                    *np.sqrt(-4 * MT**2 * MZp**2 + MZp**4))/(48. * np.pi * abs(MZp)**3) 

        
    # Zp to u
    ZPuu = (MZp**2 * (6 * gqL**2 * gZp**2 * MZp**2 + 6 * gqR**2 * gZp**2 * MZp**2))/(48. * np.pi * abs(MZp)**3)

    # Zp to c
    ZPcc = (MZp**2 * (6 * gqL**2 * gZp**2 * MZp**2 + 6 * gqR**2 * gZp**2 * MZp**2))/(48. * np.pi * abs(MZp)**3)

    # Zp to d
    ZPdd = (MZp**2 * (6 * gqL**2 * gZp**2 * MZp**2 + 6 * gqR**2 * gZp**2 * MZp**2))/(48. * np.pi * abs(MZp)**3)

    # Zp to s
    ZPss = (MZp**2 * (6 * gqL**2 * gZp**2 * MZp**2 + 6 * gqR**2 * gZp**2 * MZp**2))/(48. * np.pi * abs(MZp)**3)

    # Zp to b
    ZPbb = (MZp**2 * (6 * gqL**2 * gZp**2 * MZp**2 + 6 * gqR**2 * gZp**2 * MZp**2))/(48. * np.pi * abs(MZp)**3)

    # Zp to DM
    ZPchichi = ((-16 * gchi **2 * Mchi**2 + 4 * gchi**2 * MZp**2)
                *np.sqrt(-4 * Mchi**2 * MZp**2 + MZp**4))/(96. * np.pi * abs(MZp)**3)

    # Zp total width
    GammaZP = ZPuu + ZPcc + ZPtt + ZPdd + ZPss + ZPbb + ZPchichi


    ### spin-0 mediator ###
    Ca = np.sqrt(1 - Sa**2)
    lam1 = (Ca**2 * MH**2)/(2. * vev**2) + (MSd**2 * Sa**2)/(2. * vev**2)
    lam2 = (Ca**2 * MSd**2)/(2. * vev2**2) + (MH**2 * Sa**2)/(2. * vev2**2)
    lam3 = (Ca * (-MH**2 + MSd**2) * Sa)/(vev * vev2)

    # S to Higgs
    if MSd < 2 * MH:
        Shh = 0
    else:
        Shh = ((36 * Ca**4 * lam1**2 * Sa**2 * vev**2 - 24 * Ca**4 * lam1 * lam3 * Sa**2 * vev**2 
                + 4 * Ca**4 * lam3**2 * Sa**2 * vev**2 + 12 * Ca**2 * lam1 * lam3 * Sa**4 * vev**2 
                - 4 * Ca**2 * lam3**2 * Sa**4 * vev**2 + lam3**2 * Sa**6 * vev**2 + 12 * Ca**5 * lam1 * lam3 * Sa * vev * vev2 
                - 4 * Ca**5 * lam3**2 * Sa * vev * vev2 + 72 * Ca**3 * lam1 * lam2 * Sa**3 * vev * vev2 
                - 24 * Ca**3 * lam1 * lam3 * Sa**3 * vev * vev2 - 24 * Ca**3 * lam2 * lam3 * Sa**3 * vev * vev2 
                + 10 * Ca**3 * lam3**2 * Sa**3 * vev * vev2 + 12 * Ca * lam2 * lam3 * Sa**5 * vev * vev2 
                - 4 * Ca * lam3**2 * Sa**5 * vev * vev2 + Ca**6 * lam3**2 * vev2**2 + 12 * Ca**4 * lam2 * lam3 * Sa**2 * vev2**2 
                - 4 * Ca**4 * lam3**2 * Sa**2 * vev2**2 + 36 * Ca**2 * lam2**2 * Sa**4 * vev2**2 
                - 24 * Ca**2 * lam2 * lam3 * Sa**4 * vev2**2 + 4 * Ca**2 * lam3**2 * Sa**4 * vev2**2)
                *np.sqrt(-4 * MH**2 * MSd**2 + MSd**4))/(32. * np.pi * abs(MSd)**3)

    # S to DM
    Schichi = ((-4 * Ca**2 * Mchi**2 * ychi**2 + Ca**2 * MSd**2 * ychi**2)
                *np.sqrt(-4* Mchi**2 * MSd**2 + MSd**4))/(32. * np.pi * abs(MSd)**3)

    # S to tau
    Stautau = ((MSd**2 * Sa**2 * ytau**2 - 4 * MTA**2 * Sa**2 * ytau**2)
                *np.sqrt(MSd**4 - 4 * MSd**2 * MTA**2))/(16. * np.pi * abs(MSd)**3)

    # S to top
    if MSd < 2*MT:
        Stt = 0
    else:
        Stt = ((3 * MSd**2 * Sa**2 * yt**2 - 12 * MT**2 * Sa**2 * yt**2)
                *np.sqrt(MSd**4 - 4 * MSd**2 * MT**2))/(16. * np.pi * abs(MSd)**3)

    # S to W
    if MSd < 2*MW:
        Sww = 0
    else:
        Sww = (((3 * ee**4 * Sa**2 * vev**2)/(4. * sw**4) + (ee**4 * MSd**4 * Sa**2 * vev**2)/(16. * MW**4 * sw**4) 
                - (ee**4 * MSd**2 * Sa**2 * vev**2)/(4. * MW**2 * sw**4))
                *np.sqrt(MSd**4 - 4 * MSd**2 * MW**2))/(16. * np.pi * abs(MSd)**3)

    # S to Z
    if MSd < 2 * MZ:
        Szz = 0
    else:
        Szz = (((9 * ee**4 * Sa**2 * vev**2)/2. + (3 * ee**4 * MSd**4 * Sa**2 * vev**2)
                /(8. * MZ**4) - (3 * ee**4 * MSd**2 * Sa**2 * vev**2)/(2. * MZ**2) 
                + (3 * cw**4 * ee**4 * Sa**2 * vev**2)/(4. * sw**4) + (cw**4 * ee**4 * MSd**4 * Sa**2 * vev**2)
                /(16. * MZ**4 * sw**4) - (cw**4 * ee**4 * MSd**2 * Sa**2 * vev**2)
                /(4. * MZ**2 * sw**4) + (3 * cw**2 * ee**4 * Sa**2 * vev**2)/sw**2 
                + (cw**2 * ee**4 * MSd**4 * Sa**2 * vev**2)/(4. * MZ**4 * sw**2) 
                - (cw**2 * ee**4 * MSd**2 * Sa**2 * vev**2)/(MZ**2 * sw**2) + (3* ee**4 * Sa**2 * sw**2 * vev**2)/cw**2 
                + (ee**4 * MSd**4 * Sa**2 * sw**2 * vev**2)/(4. * cw**2*MZ**4) 
                - (ee**4 * MSd**2 * Sa**2 * sw**2 * vev**2)/(cw**2 * MZ**2) + (3 * ee**4 * Sa**2 * sw**4 * vev**2)/(4. * cw**4) 
                + (ee**4 * MSd**4 * Sa**2 * sw**4 * vev**2)/(16. * cw**4 * MZ**4) 
                - (ee**4 * MSd**2 * Sa**2 * sw**4 * vev**2)/(4. * cw**4 * MZ**2))
                *np.sqrt(MSd**4 - 4 * MSd**2 * MZ**2))/(32. * np.pi * abs(MSd)**3)


    #  S Total width
    GammaS = Shh + Schichi + Stautau + Stt + Sww + Szz


    # get BRs together in a dict

    BR_ZP = {'9000006  9000006': ZPchichi/GammaZP, 
             '5  -5': ZPbb/GammaZP,
             '4  -4': ZPcc/GammaZP,
             '3  -3': ZPss/GammaZP,
             '2  -2': ZPdd/GammaZP,
             '1  -1': ZPuu/GammaZP,
             '6  -6': ZPtt/GammaZP}
    
    BR_Sd = {'24  -24': Sww/GammaS,
             '25  25': Shh/GammaS,
             '23  23': Szz/GammaS,
             '6  -6': Stt/GammaS,
             '15  -15': Stautau/GammaS,
             '9000006  9000006': Schichi/GammaS}

    BRs = {'9900032': BR_ZP, '9900026': BR_Sd}
    widths = {'9900032': GammaZP, '9900026': GammaS}

    return BRs, widths
    

def writeParticleBlock(slhaDir):
    '''
    Function that writes block with parameters of the slha file, such as mass, couplings, quantum numbers, etc
    '''

    pass

def writeBRsBlock(slhaDir):
    '''
    Function that writes branching ratios and widths block on slha file
    '''
    pass

def writeXsecBlock(xsecNew, finalState, initialSates=['p','p'],slhaDir):
    '''
    Function that writes cross section block on slha file
    '''
    pass


# def GetXSection(Mmed=[2000], finalStates=[9900032]):
#     '''
#     Function that obtains the cross sections from interpolation given the input mass

#     :param Mmed: mediator particle mass (in GeV)
#     :param finalStatse: list of final string or PDG (e.g. ['zp'])

#     :return: mediator production cross-section (in pb)
#     '''

#     masses = {pid: 0 for pid in finalStates}
#     xsecNew = {pid: 0 for pid in finalStates}
#     for i, m in enumerate(Mmed):
#         masses[finalStates[i]] = m

#     dataScan = pd.read_pickle('./data/smodels-results/results.pcl')

#     xsecScan = dataScan[['mass.'+str(finalStates[0]), 'xsec13TeV(fb).'+str(finalStates[0])]]
#     xsecFunction = interpolate.interp1d(xsecScan['mass.'+str(finalStates[0])], xsecScan['xsec13TeV(fb).'+str(finalStates[0])])

#     for i, m in enumerate(Mmed):
#         xsecNew[finalStates[i]] = int(xsecFunction(m))/1000

#     return xsecNew

