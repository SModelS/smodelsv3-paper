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


## 2MDM Results

We used [MG5](https://launchpad.net/mg5amcnlo/) to obtain the production cross-section of both mediators of the 2MDM model, then we used the cross-sections from MG5 in the SLHA format as input for [SModelS v3](https://github.com/SModelS/smodels) in this [notebook](./notebooks/SmodelS/getResults.ipynb), and the results are stored in the pandas dataframe.

We provide also multiple results from SModelS in [data/smodelsOutput](./data/smodelsOutput). These results are then converted to a pandas DataFrame, which is used to obtain the plots using the Jupyter notebooks in the [notebooks folder](./notebooks). 

