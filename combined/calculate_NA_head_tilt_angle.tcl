##################
# This script calculates the NA head tilting angle with respect to the stalk, along the trajectory
#run as vmd -dispdev text -e calculate_NA_head_tilt_angle.tcl > log_edit
##################

clock format [clock scan now]
#set auto_path  /home/lcasalino/Software/anaconda3/lib/tcllib1.18/
#package require math
#package require math::statistics
package require Orient
namespace import Orient::orient


######################
## PDM2009: Trajectory
#
set strain_name "pdm"
set totalsimtime 441.00
set Npdbpsf "./"
set Hpdbpsf "./"

#set ali "all"
#set Ntraj "/synology2/pdm2009_H1N1_TITAN/DCD_JS/NA_all_alignment"
#set Htraj "/synology2/pdm2009_H1N1_TITAN/DCD_JS/HA_all_alignment"

#set ali "head"
#set Ntraj "./"
#set Htraj "./"

set ali "stalk"
set Ntraj "./"
set Htraj "./"


#######################
# SET TRAJECTORY STRIDE

set stride 10

#### CALCULATE head tilting angle over trajectory frames for each NA tetramer ##

for {set t 1} {$t <=1} {incr t} {

  mol new $Npdbpsf/subset.psf type psf first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all
  mol addfile $Npdbpsf/subset.pdb type pdb first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all
  mol addfile $Ntraj/alignment${ali}.dcd type dcd first 0 last -1 step $stride filebonds 1 autobonds 1 waitfor all

  # Get numframes and timestep according to stride
  set numframes [molinfo top get numframes]
  set timestep [expr {$totalsimtime/($numframes-1)}]
  puts "\n#### Numframes inc pdb: $numframes.  Timestep used: $timestep."

  puts "#### STARTING WITH TETRAMER $t ####"
  set file1 [open "headtilt.dat" w]

  for {set frame 0} {$frame < $numframes} {incr frame} {
    
    # Evolve the trajectory frame after frame
    set sim_time [expr {double($frame * $timestep)}]
    molinfo top set frame $frame 
    
    # Calculate principal exes for NA head (component 0 = X)
    set sel_head [atomselect top "name CA and ((residue 90 to 468) or (residue 559 to 937) or (residue 1028 to 1406) or (residue 1497 to 1875))"]
    set princ_head [Orient::calc_principalaxes $sel_head]
    set vhead [lindex $princ_head 0]
    set vheadmag [format "%.9f" [veclength $vhead]]

    # Calculate principal axes for NA stalk (component 2 = Z)
    set sel_stalk [atomselect top "name CA and ((residue 29 to 77) or  (residue 967 to 1015) or (residue  498 to 546) or (resid 1436 to 1484))"]
    set princ_stalk [Orient::calc_principalaxes $sel_stalk]
    set vstalk [lindex  $princ_stalk 2]
    set vstalkmag [format "%.9f" [veclength $vstalk]]

    # Calculate angle between the two vector using arcos(dotprodv1v2/(magv1*magv2)) ensuring that dotprod is positive
    set raw_dotprod [format "%.9f" [vecdot $vhead $vstalk]]
    set dotprod [if {$raw_dotprod >= 0} {set x $raw_dotprod} elseif {$raw_dotprod < 0} {set x [expr {($raw_dotprod)*(-1)}]}]
    set angle [expr {double(57.2958 * acos($dotprod / ($vstalkmag * $vheadmag)))}]

    # Print to file
    puts $file1 "[format "%.2f" $sim_time]  [format "%.5f" $angle]"
    unset sim_time vhead vheadmag princ_stalk vstalk vstalkmag dotprod angle raw_dotprod
    $sel_head delete
    $sel_stalk delete
    }
   
  mol delete top
  puts "#### Tilt Angle analysis completed for TETRAMER $t ####\n "
  close $file1
  }

clock format [clock scan now]

quit
exit
