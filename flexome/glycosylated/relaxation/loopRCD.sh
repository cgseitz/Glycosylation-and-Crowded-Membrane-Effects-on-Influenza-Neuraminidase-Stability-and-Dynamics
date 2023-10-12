#!/bin/bash

cutlist="0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0"

if [[ "$#" -ne 1 ]]; then
  echo "Usage: give a pdb filename to analyse."
  exit 1
fi

INFILE=$1
#ASSUMES EXISTENCE OF constraint files *.bond from pdb2bonds

STRIPPED=${INFILE%.pdb}
RIGID=${STRIPPED}".rcd.pdb"
POLARPML="polar.pml"
PHOBICPML="phobic.pml"

for CUT in $cutlist
do
  CUTNAME=${STRIPPED}"_cut"${CUT}".pdb"
  CUTPOLARPML="polar_cut"${CUT}".pml"
  ARGS=" $INFILE -${CUT} "
  echo $ARGS
  ./../../ForDistribution23112020/CPP/pdbRCD $ARGS
  mv $RIGID $CUTNAME
  mv $POLARPML foo
  cat foo | sed -e "s/${RIGID}/${CUTNAME}/g" > $CUTPOLARPML
  rm foo
  #NOTE: phobic.pml need not be handled because it is not cut-dependent
done
ls
