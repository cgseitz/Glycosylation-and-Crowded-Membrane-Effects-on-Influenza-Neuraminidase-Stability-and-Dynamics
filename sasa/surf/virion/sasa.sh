#!/bin/bash

module load cuda/11.3
module load amber/22

cpptraj /net/gpfs-amarolab/cseitz/from_jam/projects/influenza/neuraminidase/md/2009/whole_virion/subset.pdb sasa.in > output.log
