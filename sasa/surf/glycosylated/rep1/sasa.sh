#!/bin/bash

#module load cuda-10.1
#module load cuda/10.1
module load cuda/11.3
module load amber/22

cpptraj /net/gpfs-amarolab/cseitz/from_jam/projects/influenza/neuraminidase/md/2009/partial_glycosylation/trajectories/replicate1/no_lipids/subset.pdb sasa.in > output.log
