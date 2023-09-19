#!/bin/bash

module load amber

cpptraj step5_charmm2namd.pdb fixatomparm7.in > output.log
