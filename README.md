# smodelsv3-paper

A repository to store the code and data for the SModelS v3 physics paper,
including the Two Mediator Dark Matter (2MDM) model.

## Description

* [data](./data): data files used to obtain the paper results (SLHA files, SModelS output, MadDM output,...)
* [notebooks](./notebooks): Jupyter notebooks for plotting and processing data;
* [References](./References): Useful references;
* [scan](./scan/): Files and auxiliary code for generating the SLHA files used;

## External Packages

Currently, the following tools are necessary for running the scans:

  * [SModelS v3](https://github.com/SModelS/smodels)
  * [MadGraph5](https://launchpad.net/mg5amcnlo)
  * [MadDM](https://launchpad.net/maddm)

A slightly modified version of MadDM converted to run with Python3 is available [here](MG5_aMC_v3_5_4_maddm.tar.gz).

### 2MDM ###

## Results

We used [MG5](https://launchpad.net/mg5amcnlo/) to obtain the production cross-section of both mediators of the 2MDM model, then we used the cross-sections from MG5 in the SLHA format as input for [SModelS v3](https://github.com/SModelS/smodels) in this [notebook](./notebooks/SmodelS/getResults.ipynb), and the results are stored in the pandas dataframe.

We provide also multiple results from SModelS in [data/smodelsOutput](./data/smodelsOutput). These results are then converted to a pandas DataFrame, which is used to obtain the plots using the Jupyter notebooks in the [notebooks folder](./notebooks). 

