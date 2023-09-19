#!/bin/bash

module load amber/20

cpptraj step5_charmm2namd_reorder.parm7 diffusion.in > output.log
