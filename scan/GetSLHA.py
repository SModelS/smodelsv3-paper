#!/usr/bin/env python3

import sys, os, time, datetime
import logging
sys.path.append('../')
mg5Folder = os.path.abspath('../../MonoXSMS/MG5')
sys.path.append(mg5Folder)
from madgraph.various.banner import Banner
from configParserWrapper import ConfigParserExt
import random
import string
from scipy import interpolate
import pandas as pd
import numpy as np

FORMAT = '%(levelname)s in %(module)s.%(funcName)s(): %(message)s at %(asctime)s'
logging.basicConfig(format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger('SLHAScan')

def getXSection(mMed=2000, pid='9900032', s=13):
    '''
    Function that obtains the cross sections from interpolation given the input mass for the 2MDM model

    :param Mmed: mediator particle mass (in GeV)
    :param pid: mediator id - string
    :param s: center of mass energy, default is 13 TeV

    :return: mediator production cross-section (in pb) and energy
    '''

    xsecLabel = 'xsec'+s+'TeV(fb).'+str(pid)
    dataScan = pd.read_pickle(s+'TeV/mg5_scan_results.pcl')

    xsecScan = dataScan[['mass.'+str(pid), xsecLabel]]
    xsecFunction = interpolate.interp1d(xsecScan['mass.'+str(pid)], xsecScan[xsecLabel])

    xsecNew = int(xsecFunction(mMed))/1000

    return xsecNew, int(s)

def getBR(pars):
    '''
    Function that obtains the branching ratio for given parameters for the 2MDM model

    :param pars: dictionary to all important parameters: masses, couplings, etc

    :return: dictionary with possible branching ratios and widths
    '''
    MZp = pars['mzp']
    MSd = pars['msd']
    Mchi = pars['mchi']
    gqA = pars['gqa']
    gqV = pars['gqv']
    gchi = pars['gchi']
    Sa = pars['sa']
    ychi = pars['ychi']

    ## define constants

    # mass for quarks
    MT = 172

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
    vev2 = MZp/(2*gchi)

    # couplings
    yt = np.sqrt(2)*MT/vev
    ytau = np.sqrt(2)*MTA/vev
    gZp = 1.0

    ### spin-1 mediator ###
    gqL = (gqA + gqV)
    gqR = (-gqA + gqV)

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

    # sort BR from largest to smallest
    for pdg in BRs.keys():
        BRs[pdg] = dict(sorted(BRs[pdg].items(), key=lambda item: item[1], reverse=True))

    # write in scientific notation
    for pdg in BRs.keys():
        for finalstate, value in BRs[pdg].items():
            BRs[pdg][finalstate] = '{:e}'.format(BRs[pdg][finalstate])

    for pdg in widths.keys():
        widths[pdg] = '{:e}'.format(widths[pdg])


    return BRs, widths

def writeXsecBlock(filename, pars, energy):
    '''
    Function that writes the cross section for particles of interest based on given parameters, rescaled with the couplings
    :param pars: parameters given in parameters file
    :param filename: SLHA filename
    '''
    pdgInitial = ['2212', '2212']
    finalState = {'mzp': '9900032', 'msd': '9900026'}
    gq = 0.25
    sa = 0.25
    file = open(filename, 'a')
    for med in finalState.keys():
        xsec, sqrt = getXSection(mMed=int(pars[med]), pid=finalState[med], s=energy)
        # rescale xsec with couplings
        if med == 'mzp':
            if pars['gqv'] == 0:
                gqNew = pars['gqa']
            elif pars['gqa'] == 0:
                gqNew = pars['gqv']
            xsec = xsec*(gqNew/gq)**2
        elif med == 'msd':
            xsec = xsec*(pars['sa']/sa)**2
        xsecLine = "\nXSECTION %1.3e " %(sqrt)
        xsecLine += " ".join([pdg for pdg in pdgInitial])
        xsecLine += " 1 " 
        xsecLine += "".join(finalState[med])
        file.write(xsecLine+'\n')
        file.write("  0  0  0  0  0  303600  %1.4e madgraph 3.5.1 \n" %xsec)
        file.write('\n\n')
    file.close()

def writeBRsBlock(filename, pars):
    '''
    Function that writes the Branching Ratio for particles of interest based on given parameters
    :param pars: parameters given in parameters file
    :param filename: SLHA filename
    '''
    # get slha data from file
    file = open(filename, 'rt')
    slhaData = file.read()
    file.close()

    # get BRs and widths
    BRs, widths = getBR(pars)

    # change width
    for l in slhaData.split('\n'):
        for pdg in widths.keys():
            if not 'DECAY ' in l: continue
            if not pdg in l: continue
            oldline = l
            line = l.split()
            line[2] = ' '+str(widths[pdg])
            fixline = '  '.join(line)
            slhaData = slhaData.replace(oldline, fixline)

    for l in slhaData.split('\n'):
        for pdg in BRs.keys():
            if not 'DECAY ' in l: continue
            if not pdg in l: continue
            oldline = l
            line = '\n#  BR             NDA  ID1    ID2   ...\n'
            for finalstate, value in BRs[pdg].items():
                line += '   '+str(value)+'   2    '+finalstate+'\n'
            fixline = oldline+line
            slhaData = slhaData.replace(oldline, fixline)

    file = open(filename, 'wt')
    file.write(slhaData)
    file.close
            
def fixParams(data, oldParam, newParam):
     '''
     Function that changes the parameter in the SLHA file by the correct value
     :param data: data from SLHA file
     :string oldParam: name of the parameter that needs to be fixed
     :string newParam: correct value for parameter

     :return: fixed slha data
     '''
     slhaData = data
     for l in slhaData.split('\n'):
        if not oldParam in l: continue
        oldline = l
        line = l.split()
        line[1] = newParam
        fixline = ' '.join(line)
     slhaData = slhaData.replace(oldline, '      '+fixline)

     return slhaData

def createSLHA(parser, energy):
    '''
    Creates SLHA file with cross-section and branching ratio for parameters given in parser
    :param parser: ConfigParser object with all parameters needed
    :param energy: Center of mass energy, in TeV. Default is 13 TeV
    '''
    filename = str(energy)+'TeV/'+''.join(random.sample(string.ascii_lowercase, 8))+'.slha'
    pars = parser.toDict(raw=False)["ParamsSet"]
    baseParams = {'mzp': 2000.0, 'mchi': 65.0, 'msd': 1000.0, 'gqv': 0.0, 'gqa': 0.25,
                  'gchi': 1.6, 'ychi': 1.0, 'sa': 0.25, 'se': 0.0}
    for par in baseParams.keys():
        if par not in pars.keys():
            pars[par] = baseParams[par]

    # Create file and based on banner
    bannerFile = './default_banner.txt'
    banner = Banner()
    banner.read_banner(bannerFile)
    slhaData = banner['slha']

    # change values in banner
    slhaData = fixParams(data=slhaData, oldParam=' sd ', newParam=str('{:e}'.format(pars['msd'])))
    for param in pars.keys():
            slhaData = fixParams(data=slhaData, oldParam='# '+param, newParam=str('{:e}'.format(pars[param])))

    
    slhaF = open(filename, 'wt')
    slhaF.write(slhaData)
    slhaF.close()

    # Remove BRs from file
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        isBRblock = False
        for line in lines:
            if 'BR' in line:
                isBRblock = True
                continue
            elif line.startswith('#'):
                isBRblock = False
            if not isBRblock:
                file.write(line)
        file.truncate()
        file.close()

    # write BRs based on given parameters
    writeBRsBlock(filename, pars)

    # write Xsection block for given parameters
    writeXsecBlock(filename, pars, energy)




def main(parfile, energy, verbose):

    level = verbose
    levels = {'debug': logging.DEBUG, 'info': logging.INFO, 
              'warning': logging.WARNING, 'error': logging.ERROR}
    if not level in levels:
        logger.error('Unknown log level "%s" supplied' %level)
        sys.exit()
    logger.setLevel(level = levels[level])

    parser = ConfigParserExt(inline_comment_prefixes='#')
    ret = parser.read(parfile)
    if ret == []:
        logger.error('No such file or directory: "%s"' %args.parfile)
        sys.exit()

    # If loops have been defined, get a list of parsers
    parserList = parser.expandLoops()

    params = parser.toDict(raw=False)["ParamsSet"]
    baseParams = {"mzp": 2000.0, "mchi": 65.0, "msd": 1000.0, "gqv": 0.0, "gqa": 0.25,
                  "gchi": 1.6, "ychi": 1.0, "sa": 0.25, "se": 0.0}

    for par in baseParams.keys():
        if par not in params.keys():
            logger.info("Parameter %s not set in %s, using default value: %1.2f." %(par, args.parfile, baseParams[par]))


    now = datetime.datetime.now()
    for i,newParser in enumerate(parserList):
        r = createSLHA(newParser, energy)
        logger.info("Created SLHA file number %i/%i at %s" %(i,len(parserList),now.strftime("%Y-%m-%d %H:%M")))

    logger.info("Created all SLHA files (%i) at %s" %(len(parserList),now.strftime("%Y-%m-%d %H:%M")))

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description=
                                 "Generates a SLHA file for the parameters defined in the parameters file.")
    ap.add_argument('-p', '--parfile', default='scan_parameters_2mdm.ini',
                    help='path to the parameters file, default is [scan_parameters_2mdm.ini].')
    ap.add_argument('-s', '--energy', default='13',
                    help='center of mass energy to obtain cross section (in TeV), default is 13 TeV')
    ap.add_argument('-v', '--verbose', default='info',
                    help='verbose level (debug, info, warning or error). Default is info.')
    
    t0 = time.time()

    args = ap.parse_args()
    output = main(args.parfile, args.energy, args.verbose)

    print('\n\nDone in %3.2f min' %((time.time()-t0)/60.))





