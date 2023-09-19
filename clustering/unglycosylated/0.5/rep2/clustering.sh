#!/bin/bash

#run as ./clustering.sh

module load cuda/11.3
module load mdrun/2022.1-ubuntu
module load gromacs/2022.1-ubuntu

echo "3 0" | gmx_mpi cluster -f unglycosylated_rep2.trr -s subset.pdb -g clustering.log -dist clusteringdistance.xvg -sz clusteringsize.xvg -cl finalclusters.pdb -cutoff 0.05 -method gromos

sh frequency.sh

rm \#*
