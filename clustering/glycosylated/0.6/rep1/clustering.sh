#!/bin/bash

#run as ./clustering.sh

module load gromacs

#gmx cluster -f glycosylated.trr -s subset.pdb -g clustering.log -dist clusteringdistance.xvg -sz clusteringsize.xvg -cl finalclusters.pdb -cutoff 0.075 -method gromos
echo "3 0" | gmx_mpi cluster -f glycosylated_rep1.trr -s subset.pdb -g clustering.log -dist clusteringdistance.xvg -sz clusteringsize.xvg -cl finalclusters.pdb -cutoff 0.06 -method gromos

sh frequency.sh

rm \#*
