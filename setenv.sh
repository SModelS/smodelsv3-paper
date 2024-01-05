#!/bin/sh

currentDIR="$( pwd )"
delphesDIR=$currentDIR/home/yoxara/MG5_aMC_v3_5_1/Delphes/externals
pythiaDIR=$currentDIR/home/yoxara/MG5_aMC_v3_5_1/HEPTools/pythia8
#Make sure pythia can be found by Delphes
export LD_LIBRARY_PATH=$pythiaDIR/lib:$LD_LIBRARY_PATH
#Make sure Delphes can be found by ROOT
export ROOT_INCLUDE_PATH=$delphesDIR/external