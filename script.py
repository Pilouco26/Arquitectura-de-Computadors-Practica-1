#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# Define the simulation commands and paths in a more structured way using dictionaries.
simulators = {
    "applu": "../../exe/applu.exe < applu.in > applu.out 2> applu.err",
    "crafty": "../../exe/crafty.exe < crafty.in > crafty.out 2> crafty.err",
    "twolf": "../../exe/twolf.exe ref > ref.stdout 2> ref.err",
    "vortex": "../../exe/vortex.exe lendian1.raw > vortex1.out2 2> vortex1.err",
    "vpr": "/home/milax/Escriptori/PracticaAc/Benchmarks/vpr/exe/vpr.exe /home/milax/Escriptori/PracticaAc/Benchmarks/vpr/data/ref/net.in /home/milax/Escriptori/PracticaAc/Benchmarks/vpr/data/ref/arch.in /home/milax/Escriptori/PracticaAc/Benchmarks/vpr/data/ref/route.out -nodisp -route_only -route_chan_width 15 -pres_fac_mult 2 -acc_fac 1 -first_iter_pres_fac 4 -initial_pres_fac 8 > route_log.out 2> route_log.err"
}

paths = {
    "applu": "/home/milax/Escriptori/PracticaAc/Benchmarks/applu/data/ref",
    "crafty": "/home/milax/Escriptori/PracticaAc/Benchmarks/crafty/data/ref",
    "vpr": "/home/milax/Escriptori/PracticaAc/Benchmarks/vpr/data/ref",
    "twolf": "/home/milax/Escriptori/PracticaAc/Benchmarks/twolf/data/ref",
    "vortex": "/home/milax/Escriptori/PracticaAc/Benchmarks/vortex/data/ref"
}

processors = {
    "intel": "../../../../input/intel.txt",
    
}

# Loop through processors and simulators.
for proc, proc_config in processors.items():
    print(f"Processor: {proc}")
    for sim, sim_command in simulators.items():
        print(f"Executing: {sim}")
        
        # Change the working directory to the benchmark path.
        os.chdir(paths[sim])
        
        # Execute the simulation and redirect output to files.
        os.system(f"../../../../simplesim-3.0_acx2/sim-outorder -redir:sim "
                  f"../../../../output/{proc}-{sim}.txt -config {proc_config} "
                  f"-fastfwd 100000000 -max:inst 100000000 {sim_command}")
        
