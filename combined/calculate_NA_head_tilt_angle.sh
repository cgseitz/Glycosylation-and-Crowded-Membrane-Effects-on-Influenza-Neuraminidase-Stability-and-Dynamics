#!/bin/bash

#selecting the residue index number selected
awk -F" " '{print $1}' headtilt.dat > headtilt_time.dat
#selecting the volume values
awk -F" " '{print $2}' headtilt.dat > headtilt_angle.dat
