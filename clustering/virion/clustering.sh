#!/bin/bash

#run as ./clustering.sh

module load gromacs

gmx_mpi cluster -f virion.trr -s subset.pdb -g clustering.log -dist clusteringdistance.xvg -sz clusteringsize.xvg -cl finalclusters.pdb -cutoff 0.06 -method gromos

sh frequency.sh

rm \#*
