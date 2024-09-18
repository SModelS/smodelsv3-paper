# smodelsv3-paper

A repository to store the code and data for the SModelS v3 paper.

## Description

* [data](./data): data files used to obtain the paper results (SLHA files and SModelS output)
* [models](./models): UFO and FeynRules files for the 2MDM model;
* [notebooks](./notebooks): Jupyter notebooks for plotting and processing data;
* [scan](./scan/): Files and auxiliary code for generating the SLHA files used;

## External Packages

Currently, the following tools are necessary for running the scans:

  * [SModelS v3](https://github.com/SModelS/smodels)
  * [MadGraph5](https://launchpad.net/mg5amcnlo)


## 2MDM Results and Scan

We used [MG5](https://launchpad.net/mg5amcnlo/) to compute the production cross-sections and branching ratios for the 2MDM model.
The results were converted to the SLHA format and used as input for [SModelS v3](https://github.com/SModelS/smodels).
See [scan](./scan) for more information.

The scan results are stored in the [data](./data) folder. The SModelS output was converted to a pandas DataFrame, which was then used to obtain the plots using the Jupyter notebooks in the [notebooks folder](./notebooks). 

