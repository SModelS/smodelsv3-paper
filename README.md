# smodelsv3-paper

A repository to store the code and data for the SModelS v3 physics paper,
including the Two Mediator Dark Matter (2MDM) model.

## Description

* [data](./data): Data files used for plotting;
* [notebooks](./notebooks): Jupyter notebooks for some plots and  to gather other data;
* [References](./References): Useful references;
* [scan](./scan/): Information about scan perfomed to obtain SLHA files used to obtain results with SModelS v3;
* [parameters_2mdm.ini](./parameters_2mdm.ini): Parameters file for the 2MDM model used in SModelS.

## External Packages

Currently, the following tools are necessary for running the scans:

  * [SModelS v3](https://github.com/SModelS/smodels)

### 2MDM ###

[Overview of the Two-Mediator Dark Matter Model (2MDM): Symmetries, Interactions, Parameters, and results](https://www.overleaf.com/read/xszpmbtnpmhn)

[Slides](https://www.overleaf.com/read/vgwmdhjrzsdm#c9e46c)

## Results
We used [MG5](https://launchpad.net/mg5amcnlo/) to obtain the production cross-section of both mediators of the 2MDM model, then we used the cross-sections from MG5 in the SLHA format as input for [SModelS v3](https://github.com/SModelS/smodels) in this [notebook](./notebooks/SmodelS/getResults.ipynb), and the results are stored in the pandas dataframe.

We provide also multiple results from SModelS in [smodels_results.tgz](./data/smodels_results.tgz). These results are presented as a pandas DataFrame, and notebooks used to create relevant plots can be found in the [SmodelS](./notebooks/SmodelS) folder. 

