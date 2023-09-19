#!/bin/bash

#run as ./clustering.sh

module load gromacs

gmx pdb2gmx -f subset.pdb -o subset.gro -ignh -p subset.top
with the ff99SB force field, option 5
#gmx mk_angndx -s subset.pdb -n index.ndx -type dihedral

#gmx cluster -f glycosylated.trr -s subset.pdb -g clustering.log -dist clusteringdistance.xvg -sz clusteringsize.xvg -cl finalclusters.pdb -cutoff 0.2 -method gromos

#sh frequency.sh

#rm \#*
