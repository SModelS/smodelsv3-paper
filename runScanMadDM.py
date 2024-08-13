#!/usr/bin/env python3

# 1) Run MadGraph using the options set in the input file 
# (the proc_card.dat, parameter_card.dat and run_card.dat...).

from __future__ import print_function
import sys,os,glob
from configParserWrapper import ConfigParserExt
import logging,shutil
import subprocess
import multiprocessing
import tempfile
import time,datetime

FORMAT = '%(levelname)s in %(module)s.%(funcName)s(): %(message)s at %(asctime)s'
logging.basicConfig(format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger("MG5Scan")


def runMadDM(parser):
    
    """
    Runs MadDM.
    
    :param parser: Dictionary with parser sections.
    
    :return: True if successful. Otherwise False.
    """

    
    t0 = time.time()
    pars = parser["MadDMPars"]
    if not 'runFolder' in pars:
        logger.error('Run folder not defined.')
        return False        
    else:
        runFolder = pars['runFolder']

    if not 'maddmFolder' in pars:
        logger.error('maddmFolder folder not defined.')
        return False        
    else:
        maddmFolder = pars['maddmFolder']
        if not os.path.isdir(maddmFolder):
            logger.error('MadDM folder %s not found.' %maddmFolder)
            return False            

    # If run folder does not exist, create it using processFolder as a template:
    if not os.path.isdir(runFolder):
        runFolder = shutil.copytree(maddmFolder,runFolder,
                                    ignore=shutil.ignore_patterns('output'),
                                    symlinks=True)
        os.makedirs(os.path.join(runFolder,'output'))
        logger.info("Created temporary folder %s" %runFolder) 
            
    if not os.path.isdir(runFolder):
        logger.error('Run folder %s not found.' %runFolder)
        return False

    if 'maddmcard' in pars and os.path.isfile(pars['maddmcard']):    
        shutil.copyfile(pars['maddmcard'],os.path.join(runFolder,'Cards/maddm_card.dat'))
    if 'paramcard' in pars and os.path.isfile(pars['paramcard']):
        shutil.copyfile(pars['paramcard'],os.path.join(runFolder,'Cards/param_card.dat'))    
    
    logger.info("Running MadDM")
    run = subprocess.Popen('./maddm.x',
                           shell=True,stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,cwd=runFolder)
      
    output,errorMsg= run.communicate()
    runInfo = {'time (s)' : time.time()-t0}
    runInfo.update(pars)

    logger.debug(f'MadDM error:\n %s \n' %errorMsg.decode("utf-8"))
    logger.debug(f'MadDM output:\n %s \n' %output.decode("utf-8"))
      

    return runInfo

def moveFolders(runInfo):
    """
    Move the run folders from the temporary running folder
    to the MadDM folder.
    """

    logger.info('Finished MadDM run %i in %1.2f min' 
                %(int(runInfo['runNumber']),runInfo['time (s)']/60.))

    # Get run folder:
    runFolder = os.path.abspath(runInfo['runFolder'])
    runNumber = int(runInfo['runNumber'])
    maddmFolder = os.path.abspath(runInfo['maddmFolder'])
    # If run folder and process folder are the same, do nothing
    if runFolder == maddmFolder:
        return
    
    # Move run folder results to process folder
    runDir = os.path.join(runFolder,'output')
    if not os.path.isdir(runDir):
        logger.error(f"Error. Output folder {runDir} not found")
        return False
    # Store param_card.dat in runDir
    shutil.copy(os.path.join(runFolder,'Cards','param_card.dat'),runDir)
    finalRunDir = os.path.join(maddmFolder,'run_%02d' %runNumber)
    logger.info('Moving %s to %s' %(runDir,finalRunDir))
    shutil.move(runDir,finalRunDir)
    logger.info('Deleting temporary folder %s' %(runFolder))
    shutil.rmtree(runFolder)


def main(parfile,verbose):
   
    level = verbose
    levels = { "debug": logging.DEBUG, "info": logging.INFO,
               "warn": logging.WARNING,
               "warning": logging.WARNING, "error": logging.ERROR }
    if not level in levels:
        logger.error ( "Unknown log level ``%s'' supplied!" % level )
        sys.exit()
    logger.setLevel(level = levels[level])    

    parser = ConfigParserExt(inline_comment_prefixes="#")   
    ret = parser.read(parfile)
    if ret == []:
        logger.error( "No such file or directory: '%s'" % args.parfile)
        sys.exit()
            
    #Get a list of parsers (in case loops have been defined)    
    parserList = parser.expandLoops()

    # Start multiprocessing pool
    ncpus = -1
    if parser.has_option("options","ncpu"):
        ncpus = int(parser.get("options","ncpu"))
    if ncpus  < 0:
        ncpus =  multiprocessing.cpu_count()
    ncpus = min(ncpus,len(parserList))
    pool = multiprocessing.Pool(processes=ncpus)
    if ncpus > 1:
        logger.info('Running in parallel with %i processes' %ncpus)
    else:
        logger.info('Running in series with a single process')

    now = datetime.datetime.now()
    children = []
    for irun,newParser in enumerate(parserList):
        maddmFolder = newParser.get('MadDMPars','maddmFolder')
        maddmFolder = os.path.abspath(maddmFolder)
        if maddmFolder[-1] == '/':
            maddmFolder = maddmFolder[:-1]
        if not os.path.isdir(maddmFolder):
            logger.error('Folder %s not found. Create the folder before running the scan' %maddmFolder)
            return False

        # Get largest existing output folder:
        run0 = 1
        runsFolder = os.path.join(maddmFolder,'output')
        if os.path.isdir(runsFolder):
            for runF in glob.glob(os.path.join(runsFolder,'run*')):
                run0 = max(run0,int(os.path.basename(runF).replace('run_',''))+1)

        # Create temporary folder names if running in parallel
        if ncpus > 1:
            # Create temporary folders
            runFolder = tempfile.mkdtemp(prefix='%s_'%(maddmFolder),suffix='_run_%02d' %(run0+irun))
            os.removedirs(runFolder)
        else:
            runFolder = maddmFolder

        newParser.set('MadDMPars','runFolder',runFolder)
        newParser.set('MadDMPars','runNumber','%02d' %(run0+irun))

        parserDict = newParser.toDict(raw=False)
        logger.debug('submitting with pars:\n %s \n' %parserDict)
        p = pool.apply_async(runMadDM, args=(parserDict,), callback=moveFolders)                       
        children.append(p)

#     Wait for jobs to finish:
    output = [p.get() for p in children]
    logger.info("Finished all runs (%i) at %s" %(len(parserList),now.strftime("%Y-%m-%d %H:%M")))

    return output
    


if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser( description=
            "Run a (serial) MadDM scan for the parameters defined in the parameters file." )
    ap.add_argument('-p', '--parfile', default='scan_parameters_MadDM.ini',
            help='path to the parameters file [scan_parameters_MadDM.ini].')
    ap.add_argument('-v', '--verbose', default='info',
            help='verbose level (debug, info, warning or error). Default is info')


    
    t0 = time.time()

    args = ap.parse_args()
    output = main(args.parfile,args.verbose)
            
    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))
