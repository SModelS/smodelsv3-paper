#!/usr/bin/env python3
#/home/yoxara/2MDM/xsecSd.py

base_path = "/home/yoxara/2MDM"
file_path = f"{base_path}/scripts/sigmaSd.txt"

MSd_values = [140, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2400]
Sa_values = [0.2]

with open(file_path, "w") as f:
    f.write(f"import {base_path}/models/Feynrules/2MDM/2MDMNLO -modelname\n")
    f.write("define p = g u c d s b u~ c~ d~ s~ b~\n")
    f.write("define j = p \n")
    f.write("generate p p > Sd [noborn=QCD]\n")
    f.write(f"output sigmaSdXdXdjnlo\n")
    f.write(f"launch sigmaSdXdXdjnlo\n")
    #f.write(f"shower = Pythia8\n")
    #f.write(f"detector = Delphes\n")
    f.write("analysis = ExRoot\n")
    f.write("set run_card nevents 10000\n")
    f.write("set run_card ebeam1 6500\n")
    f.write("set run_card ebeam2 6500\n")
    f.write("set run_card lpp1 1\n")
    f.write("set run_card lpp2 1\n")    
    f.write("set run_card pdlabel lhapdf\n")
    f.write("set run_card lhaid 303600\n")
    f.write("set run_card scale 91.188\n")
    f.write("set run_card dsqrt_q2fact1 91.188\n")
    f.write("set run_card dsqrt_q2fact2 91.188\n")
    f.write("set run_card scalefact 1.0\n")    
    f.write("set run_card nhel 0\n")
    f.write("set run_card sde_strategy 2\n")    
    f.write("set run_card bwcutoff 15.0\n")    
    f.write("set run_card maxjetflavor 5\n")
    f.write("set param_card ychi 1\n")
    f.write("set param_card Mchi 65\n")
    f.write("set param_card gchi 1\n")
    f.write("set param_card MZp 2000\n")

    for j in Sa_values:
        for i in MSd_values:
            f.write(f"set param_card MSd {i}\n")
            f.write(f"set param_card WSd auto \n")
            f.write(f"set param_card Sa {j}\n")
            f.write("done\n")
            if i !=  MSd_values[-1] or j != Sa_values[-1] :
                f.write("launch\n")
                
    f.write(f"launch {base_path}/2mdm_sigmaSd -i\n")
    f.write(f"print_results --path={base_path}/data/sigmaSd.txt --format=short\n")
    f.write("exit\n")