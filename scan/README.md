## Description

This folder is dedicated to create the SLHA files used to obtain the results of this paper. It contains the following subdirectory:

* [MG5_scan](./MG5_scan): Folder for performing scans using MadGraph5;
* [configParserWrapper.py](./configParserWrapper.py): Auxiliar code for parsing through elements in [parameters file](./scan_parameters_2mdm.ini);
* [getSLHA.py](./getSLHA.py): script to obtain SLHA files with production cross-section without running MG5;
* [default_banner.txt](./default_banner.txt): text file in SLHA format used as template for SLHA files creation;
* [mg5_scan.pcl]: Pickle file containing the two mediatiors production cross-sections used as data points for interpolation in [getSLHA.py](./getSLHA.py); 


Here one finds all files necessary to obtain SLHA files for the 2MDM model, including the cross-section for production of both mediators. The SLHA files can be generated using the [createSLHA.py](./createSLHA.py) script, or using MadGraph5 (MG5) via the script [runScanMG5.py](./MG5_scan/runScanMG5.py). The former option is the fastest one, since no MG5 run is needed to be perfomed, however, in both cases the installation of MG5 is required.

## Running the scans

In order to obtain the SLHA files, one must simply run the [getSLHA.py](./getSLHA.py) script using as parameter the [parameters file](./scan_parameters_2mdm.ini). One example is to type the command line in terminal:
```
./getSLHA.py -p scan_parameters_2mdm.ini
```
As mentioned previously, the MG5 package is required even though no Monte Carlo simulation is performed. Therefore, the respective MG5 path must be indicated in the line 6 of the [getSLHA.py](./getSLHA.py) script. The parameters used to create the SLHA files are set in [scan_parameters_2mdm.ini](./scan_parameters_2mdm.ini), such as the mediators and dark matter masses, the coupling parameters, as well as the output folder of the SLHA files. The cross-sections are obtained via 1D interpolation, and rescaled for the selected couplings if necessary. Cross sections for 13TeV and 8TeV are provided for both mediators, as well as the Branching Ratios for the possible 2-body decays. 

