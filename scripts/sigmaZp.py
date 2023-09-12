#!/usr/bin/env python3
#/home/yoxara/2MDM/xsecZp.py
base_path = "/home/yoxara/2MDM"
file_path = f"{base_path}/scripts/sigmaZp.txt"
MZp_values = list(range(500, 3500, 500))
gqV_values = [0.1,0.2]
with open(file_path, "w") as f:
    f.write(f"import {base_path}/models/Feynrules/2MDM/2MDM -modelname\n")
    f.write("define p = g u c d s b u~ c~ d~ s~ b~\n")
    f.write("define j = g u c d s b u~ c~ d~ s~ b~\n")
    f.write("generate p p > zp j\n")
    f.write(f"output sigmaZp\n")
    f.write(f"launch sigmaZp\n")
    f.write(f"shower = Pythia8\n")
    f.write(f"detector = Delphes\n")
    f.write("analysis = ExRoot\n")
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
    f.write("set param_card gqA 0\n")
    f.write("set param_card ychi 1\n")
    f.write("set param_card Mchi 200\n")
    f.write("set param_card gchi 0.5\n")

    for i in MZp_values:
        for j in gqV_values:
            f.write(f"set param_card MZp {i}\n")
            f.write(f"set param_card WZp auto\n")
            f.write(f"set param_card gqV {j}\n")
            f.write("done\n")
            if i !=  MZp_values[-1] or j != gqV_values[-1] :
                f.write("launch\n")
                
    f.write(f"launch sigmaZp -i\n")
    f.write(f"print_results --path={base_path}/data/sigmaZp.txt --format=short\n")
    f.write("exit\n")