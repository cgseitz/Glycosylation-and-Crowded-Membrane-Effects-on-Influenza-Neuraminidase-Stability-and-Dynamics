#!/bin/bash

#run as ./clustering.sh

module load cuda/11.3
module load mdrun/2022.1-ubuntu
module load gromacs/2022.1-ubuntu 

#gmx cluster -f glycosylated.trr -s subset.pdb -g clustering.log -dist clusteringdistance.xvg -sz clusteringsize.xvg -cl finalclusters.pdb -cutoff 0.075 -method gromos
echo "3 0" | gmx_mpi cluster -f glycosylated_rep3.trr -s subset.pdb -g clustering.log -dist clusteringdistance.xvg -sz clusteringsize.xvg -cl finalclusters.pdb -cutoff 0.06 -method gromos

sh frequency.sh

rm \#*
