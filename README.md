# smodelsv3-paper

A repository to store the code and data for the SModelS v3 physics paper,
including the Two Mediator Dark Matter (2MDM) model.

## Description

* [Cards](./Cards): Cards for generating events with MadGraph5;
* [models](./models): UFO and FeynRules files for the implemented model;
* [notebooks](./notebooks): Jupyter notebooks for some plots and  to gather other data;
* [data](./data): Data files used for plotting;
* [References](./References): Useful references.

## External Packages

Currently the following tools are necessary for running the scans:

  * [MadGraph5](https://launchpad.net/mg5amcnlo/)
  * [SModelS v3](https://github.com/SModelS/smodels)

### 2MDM ###

[Overview of the Two-Mediator Dark Matter Model (2MDM): Symmetries, Interactions, Parameters, and results](https://www.overleaf.com/read/xszpmbtnpmhn)


## Running the scans
 In order to obtain the SLHA files and perform analysis using SModelS, one must first generate data points using the files with '.ini' extension. To generate its own data points, simply run the comand line on the terminal:
```
./runScanMG5.py -p <parameters-file.ini>
```
and then extracting relevant data for the SLHA file using the [createSLHA.py](./createSLHA.py) script:
```
./createSLHA.py -f <list of .lhe.gz or banner.txt files>
```
Finally, the SModelS is used in this (notebook)[./notebooks/SmodelS/getResults.ipynb] and the results are stored in a pandas dataframe.

Alternatively, multiple results from SModelS can be found in [smodels_results.tgz](./data/smodels_results.tgz), by simply extracting the compressed folder. These results are presented as a pandas DataFrame, and notebooks used to create relevant plots can be found in the [SmodelS](./notebooks/SmodelS) folder. 

