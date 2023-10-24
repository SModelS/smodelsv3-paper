# smodelsv3-paper

A repository to store the code and data for the SModelS v3 physics paper,
including the Two Mediator Dark Matter (2MDM) model.


[Overview of the Two-Mediator Dark Matter Model (2MDM): Symmetries, Interactions, Parameters, and results](https://www.overleaf.com/read/xszpmbtnpmhn)

## Description

* [Cards](./Cards): Cards for generating events with MadGraph5;
* [models](./models): UFO and FeynRules files for the implemented model;
* [notebooks](./notebooks): Jupyter notebooks for some plots and  to gather other data;
* [data](./data): Data files used for plotting;
* [References](./References): Useful references.


## Scan Data ##

The data for the 2MDM scan can be downloaded from CERNBox
using:

``
wget https://cernbox.cern.ch/xxxx

## Results and Plotting ##

### 2MDM ###

## Running the scans

### Basic Installation ###

The script installer.sh will try to fetch and install the following packages:

  * [smodels](https://smodels.github.io/)



### 2MDM scan ###

The main scripts generating the SLHA files using SoftSUSY and computing the cross-sections (using SModelS or Prospino) are:

The input of the above scripts are controlled by par (.ini) files stored in the [EWino](EWino) folder.    

The SModelS output is computed using the runSModelS.py script with this [parameter file](EWino/smodels_parameters.ini)
....
