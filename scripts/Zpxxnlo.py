#!/usr/bin/env python3
#/home/yoxara/smodels/SmodelSSMS/2MDM/xsecZp.py

base_path = "/home/yoxara/smodels/SmodelSSMS/2MDM"
file_path = f"{base_path}/scripts/Zpxx.txt"

MZp_values = list(range(250, 4000, 250))
gq_values = [0.005,0.05, 0.1, 0.5]

with open(file_path, "w") as f:
    # Initial setup
    f.write(f"import {base_path}/Feynrules/2MDM/2MDM -modelname\n")
    f.write("define p = g u c d s b u~ c~ d~ s~ b~\n")
    f.write("generate p p > zp > chi chi @1\n")
    f.write(f"output Zpxx\n")
    f.write(f"launch Zpxx\n")
    f.write("analysis = MadAnalysis4\n")
    f.write("shower Pythia8\n")
    f.write("detector Delphes\n")
    f.write("set run_card nevents 15000\n")
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
    f.write("set param_card gZp 1\n")
    f.write("set param_card gchi 1\n")
    f.write("set param_card MZp 2000\n")
    f.write("set param_card Mchi 250\n")
    f.write("set param_card ychi 1\n")
    
    for i in MZp_values:
        for j in gq_values:
            f.write(f"set param_card MZp {i}\n")
            f.write(f"set param_card gq {j}\n")
            f.write("done\n")
            if i !=  MZp_values[-1] or j != gq_values[-1] :
                f.write("launch\n")

    f.write(f"launch Zpxx -i\n")
    f.write(f"print_results --path={base_path}/data/Zpxx.txt --format=short\n")
    f.write("exit\n")