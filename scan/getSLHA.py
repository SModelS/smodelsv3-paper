#!/usr/bin/env python3

import sys, os, time, datetime
import logging
from configParserWrapper import ConfigParserExt
from scipy import interpolate
import pandas as pd
import numpy as np
import tempfile
import progressbar as P

FORMAT = '%(levelname)s in %(module)s.%(funcName)s(): %(message)s at %(asctime)s'
logging.basicConfig(format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger('SLHAScan')


def getBR(pars):
    '''
    Function that obtains the branching ratio for given parameters for the 2MDM model

    :param pars: dictionary to all important parameters: masses, couplings, etc

    :return: dictionary with possible branching ratios and widths
    '''
    MZp = pars['mzp']
    MSd = pars['msd']
    Mchi = pars['mchi']
    gq = pars['gq']
    gchi = pars['gchi']
    sina = pars['sina']
    ychi = 2 * np.sqrt(2) * gchi * Mchi / MZp

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
    aEW = 1 / aEWM1
    ee = 2 * np.sqrt(aEW) * np.sqrt(np.pi)

    sw2 = 1 - MW**2 / MZ**2
    sw = np.sqrt(sw2)
    cw = np.sqrt(1 - sw2)

    # vevs
    vev = (2 * MW * sw) / ee
    vev2 = MZp/(2*gchi)

    # couplings
    yt = np.sqrt(2) * MT / vev
    ytau = np.sqrt(2) * MTA / vev
    gZp = 1.0

    ### spin-1 mediator ###
    gqL = (gqA + gqV)
    gqR = (-gqA + gqV)
    QBphi = (-2 * gchi) / gZp
    QBq = gq / gZp
    QBchi = gchi / gZp

    # Zp to t 
    if MZp < 2*MT:
        ZPtt = 0
    else:
        ZPtt = ((24 * gZp**2 * MT**2 * QBq**2 + 12 * gZp**2 * MZp**2 * QBq**2)*np.sqrt(-4 * MT**2 * MZp**2 + MZp**4))/(48. * np.pi * abs(MZp)**3)

        
    # Zp to u
    ZPuu = (gZp**2 * MZp**4 * QBq**2)/(4. * np.pi * abs(MZp)**3)

    # Zp to c
    ZPcc = (gZp**2 * MZp**4 * QBq**2)/(4. * np.pi * abs(MZp)**3)

    # Zp to d
    ZPdd = (gZp**2 * MZp**4 * QBq**2)/(4. * np.pi * abs(MZp)**3)
    
    # Zp to s
    ZPss = (gZp**2 * MZp**4 * QBq**2)/(4. * np.pi * abs(MZp)**3)
    
    # Zp to b
    ZPbb = ((24 * gZp**2 * MB**2 * QBq**2 + 12 * gZp**2 * MZp**2 * QBq**2)*np.sqrt(-4 * MB**2 * MZp**2 + MZp**4))/(48. * np.pi * abs(MZp)**3)

    # Zp to DM
    if MZp < 2*Mchi:
        ZPchichi = 0
    else:
        ZPchichi = ((-16 * gchi**2 * Mchi**2 + 4 * gchi**2 * MZp**2) * np.sqrt(-4 * Mchi**2 * MZp**2 + MZp**4))/(96. * np.pi * abs(MZp)**3)

    # Zp total width
    GammaZP = ZPuu + ZPcc + ZPtt + ZPdd + ZPss + ZPbb + ZPchichi


    ### spin-0 mediator ###
    cosa = np.sqrt(1 - sina**2)
    lam1 = (cosa**2 * Mh**2)/(2. * vev**2) + (MSd**2 * sina**2)/(2. * vev**2)
    lam2 = (cosa**2 * MSd**2)/(2. * vev2**2) + (Mh**2 * sina**2)/(2. * vev2**2)
    lam3 = (cosa * (-Mh**2 + MSd**2) * sina)/(vev * vev2)

    # S to Higgs
    if MSd < 2 * MH:
        Shh = 0
    else:
        Shh = ((36 * cosa**4 * lam1**2 * sina**2 * vev**2 - 24 * cosa**4 * lam1 * lam3 * sina**2 * vev**2 + 4 * cosa**4 * lam3**2 * sina**2 * vev**2 + 12 * cosa**2 * lam1 * lam3 * sina**4 * vev**2 - 4 * cosa**2 * lam3**2 * sina**4 * vev**2 + lam3**2 * sina**6 * vev**2 + 12 * cosa**5 * lam1 * lam3 * sina * vev * vev2 - 4 * cosa**5 * lam3**2 * sina * vev * vev2 + 72 * cosa**3 * lam1 * lam2 * sina**3 * vev * vev2 - 24 * cosa**3 * lam1 * lam3 * sina**3 * vev * vev2 - 24 * cosa**3 * lam2 * lam3 * sina**3 * vev * vev2 + 10 * cosa**3 * lam3**2 * sina**3 * vev * vev2 + 12 * cosa * lam2 * lam3 * sina**5 * vev * vev2 - 4 * cosa * lam3**2 * sina**5 * vev * vev2 + cosa**6 * lam3**2 * vev2**2 + 12 * cosa**4 * lam2 * lam3 * sina**2 * vev2**2 - 4 * cosa**4 * lam3**2 * sina**2 * vev2**2 + 36 * cosa**2 * lam2**2 * sina**4 * vev2**2 - 24 * cosa**2 * lam2 * lam3 * sina**4 * vev2**2 + 4 * cosa**2 * lam3**2 * sina**4 * vev2**2) * np.sqrt(-4 * Mh**2 * MSd**2 + MSd**4))/(32. * np.pi * abs(MSd)**3)

    # S to DM
    if MSd < 2*Mchi:
        Schichi = 0
    else:
        Schichi = ((-4 * cosa**2 * Mchi**2 * ychi**2 + cosa**2 * MSd**2 * ychi**2) * np.sqrt(-4 * Mchi**2 * MSd**2 + MSd**4))/(32. * np.pi * abs(MSd)**3)
                    

    # S to tau
    Stautau = ((MSd**2 * sina**2 * ytau**2 - 4 * MTA**2 * sina**2 * ytau**2) * np.sqrt(MSd**4 - 4 * MSd**2 * MTA**2))/(16. * np.pi * abs(MSd)**3)

    # S to top
    if MSd < 2*MT:
        Stt = 0
    else:
        Stt = ((3 * MSd**2 * sina**2 * yt**2 - 12 * MT**2 * sina**2 * yt**2) * np.sqrt(MSd**4 - 4 * MSd**2 * MT**2))/(16. * np.pi * abs(MSd)**3)

    # S to W
    if MSd < 2*MW:
        Sww = 0
    else:
        Sww = (((3 *ee**4 * sina**2 * vev**2)/(4. * sw**4) + (ee**4 * MSd**4 * sina**2 * vev**2)/(16. * MW**4 * sw**4) - (ee**4 * MSd**2 * sina**2 * vev**2)/(4. * MW**2 * sw**4)) * np.sqrt(MSd**4 - 4 * MSd**2 * MW**2))/(16. * np.pi * abs(MSd)**3)

    # S to Z
    if MSd < 2 * MZ:
        Szz = 0
    else:
        Szz = (((9 * ee**4 * sina**2 * vev**2)/2. + (3 * ee**4 * MSd**4 * sina**2 * vev**2)/(8. * MZ**4) - (3 * ee**4 * MSd**2 * sina**2 * vev**2)/(2. * MZ**2) + (3 * cw**4 * ee**4 * sina**2 * vev**2)/(4. * sw**4) + (cw**4 * ee**4 * MSd**4 * sina**2 * vev**2)/(16. * MZ**4 * sw**4) - (cw**4 * ee**4 * MSd**2 * sina**2 * vev**2)/(4. * MZ**2 * sw**4) + (3 * cw**2 * ee**4 * sina**2 * vev**2)/sw**2 + (cw**2 * ee**4 * MSd**4 * sina**2 * vev**2)/(4. * MZ**4 * sw**2) - (cw**2 * ee**4 * MSd**2 * sina**2 * vev**2)/(MZ**2 * sw**2) + (3 * ee**4 * sina**2 * sw**2 * vev**2)/cw**2 + (ee**4 * MSd**4 * sina**2 * sw**2 * vev**2)/(4. * cw**2 * MZ**4) - (ee**4 * MSd**2 * sina**2 * sw**2 * vev**2)/(cw**2 * MZ**2) + (3 * ee**4 * sina**2 * sw**4 * vev**2)/(4. * cw**4) + (ee**4 * MSd**4 * sina**2 * sw**4 * vev**2)/(16. * cw**4 * MZ**4) - (ee**4 * MSd**2 * sina**2 * sw**4 * vev**2)/(4. * cw**4 * MZ**2)) * np.sqrt(MSd**4 - 4 * MSd**2 * MZ**2))/(32. * np.pi * abs(MSd)**3)
    if MSd < 2 * MZp:
         Szpzp = 0
    else:
         Szpzp = ((12 * cosa**2 * gZp**4 * QBphi**4 * vev2**2 + (cosa**2 * gZp**4 * MSd**4 * QBphi**4 * vev2**2)/MZp**4 - (4 * cosa**2 * gZp**4 * MSd**2 * QBphi**4 * vev2**2)/MZp**2) * np.sqrt(MSd**4 - 4 * MSd**2 * MZp**2))/(32. * np.pi * abs(MSd)**3)


    #  S Total width
    GammaS = Shh + Schichi + Stautau + Stt + Sww + Szz + Szpzp


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
             '9000006  9000006': Schichi/GammaS,
             '9900032  9900032': Szpzp/GammaS}

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

def writeXsecBlock(filename, pars, xsecs):
    '''
    Function that writes the cross section for particles of interest based on given parameters, rescaled with the couplings
    :param pars: parameters given in parameters file
    :param filename: SLHA filename
    :param xsecs: dictionary with interpolation functions for cross-section
    '''
    pdgInitial = ['2212', '2212']
    finalState = {'mzp': '9900032', 'msd': '9900026'}
    mMeds = {'mzp': pars['mzp'], 'msd': pars['msd']}
    gq = 0.25
    sina = 0.2
    file = open(filename, 'a')
    # iterates over final state mediators and their respective IDs 
    for med, particle in finalState.items():
        # iterates over CoM energies and the xsecs functions dictionary
        for energy, xsecDict in xsecs.items():
            # gets the xsec value for a particle ID at given CoM energy. divides the number by 1000 so the result is in pb
            xsec = xsecDict[particle](mMeds[med])/1000 
            # rescale xsec with couplings
            if med == 'mzp':
                if pars['gq'] == 0:
                    gqNew = pars['gq']']
                xsec = xsec*(gqNew/gq)**2
            elif med == 'msd':
                xsec = xsec*(pars['sina']/sina)**2
            xsecLine = "\nXSECTION %1.3e " %(int(energy)*1000)
            xsecLine += " ".join([pdg for pdg in pdgInitial])
            xsecLine += " 1 " 
            xsecLine += "".join(particle)
            file.write(xsecLine+'\n')
            file.write("  0  0  0  0  0  0  %1.4e madgraph 3.5.3 \n" %xsec)
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
                if float(value) == 0.0: continue
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

def createSLHA(parser, xsecs):
    '''
    Creates SLHA file with cross-section and branching ratio for parameters given in parser
    :param parser: ConfigParser object with all parameters needed
    '''
    pars = parser.toDict(raw=False)['slhaCreator']
    slhaFolder = pars['outputFolder']
    try:
         os.makedirs(slhaFolder)
    except:
         pass

    filename = tempfile.NamedTemporaryFile(mode= 'w+b', prefix='scan_', suffix='.slha', delete=False, dir=slhaFolder).name
    params = parser.toDict(raw=False)['ParamsSet']
    baseParams = {'mzp': 2000.0, 'mchi': 65.0, 'msd': 1000.0, 'gq': 0.25,
                  'gchi': 1.414214, 'sina': 0.2, 'se': 0.0}
    for par in baseParams.keys():
        if par not in params.keys():
            params[par] = baseParams[par]

    # make sure all parameters are floats
    for par in params.keys():
        params[par] = float(params[par])

    # Create slha file based on template
    template = open('template.slha', 'r')
    slhaData = template.read()
    template.close()
    

    # change values in banner
    slhaData = fixParams(data=slhaData, oldParam=' sd ', newParam=str('{:e}'.format(params['msd'])))
    for param in params.keys():
            slhaData = fixParams(data=slhaData, oldParam='# '+param, newParam=str('{:e}'.format(params[param])))

    slhaF = open(filename, 'wt')
    slhaF.write(slhaData)
    slhaF.close()

    # write BRs based on given parameters
    writeBRsBlock(filename, params)

    # write Xsection block for given parameters
    writeXsecBlock(filename, params, xsecs)




def main(parfile, verbose):

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


    # define default parameters
    params = parser.toDict(raw=False)["ParamsSet"]
    baseParams = {"mzp": 2000.0, "mchi": 65.0, "msd": 1000.0, "gq": 0.25,
                  "gchi": 1.414214, "sina": 0.25, "se": 0.0}

 

    for par in baseParams.keys():
        if par not in params.keys():
            logger.info("Parameter %s not set in %s, using default value: %1.2f." %(par, args.parfile, baseParams[par]))



    # initialize progressbar
    now = datetime.datetime.now()
    progressbar = P.ProgressBar(widgets=["Creating SLHA file(s): ", P.Percentage(),
                                P.Bar(marker=P.RotatingMarker()), P.ETA()])
    progressbar.maxval = len(parserList)
    progressbar.start()
    
    # obtain function for cross-section
    xsecData = pd.read_pickle('mg5_scan.pcl')

    xsecs = {'13': {},'8': {}}
    pid = ['9900026', '9900032']
    # create dictionary that contains for each CoM energy another dict with the particles IDs as keys and their respective xsec function as element
    for s in xsecs.keys():
        for particle in pid:
            xsecs[s][particle] = interpolate.interp1d(xsecData['mass.'+particle], xsecData['xsec'+s+'TeV(fb).'+particle], 
                                                     kind='linear', bounds_error=True)
        
    for i,newParser in enumerate(parserList):
        progressbar.update(i)
        r = createSLHA(newParser, xsecs)

    progressbar.finish()

    logger.info("\nCreated all SLHA files (%i) at %s" %(len(parserList),now.strftime("%Y-%m-%d %H:%M")))

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description=
                                 'Generates a SLHA file for the parameters defined in the parameters file.'
                                +' The cross-sections are obtained from an 1D interpolation using base values generated with MG5, '
                                +'and then rescaled (if necessary) according to given coupling between mediators and quarks.')
    ap.add_argument('-p', '--parfile', default='scan_parameters_2mdm.ini',
                    help='path to the parameters file, default is [scan_parameters_2mdm.ini].')
    ap.add_argument('-v', '--verbose', default='info',
                    help='verbose level (debug, info, warning or error). Default is info.')
    
    t0 = time.time()

    args = ap.parse_args()
    output = main(args.parfile, args.verbose)

    print('\n\nDone in %3.2f min' %((time.time()-t0)/60.))





