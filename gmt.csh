#!/bin/csh -f
#

# Set the output file
set psfile = "./gmt.ps"

# Start the Postscript file 
# 
psbasemap -JM6.5i -R-111.358/-103.995/19.039/24.561 -Ba2.000f2.000/a1.000f1.000NEWS:."":  -X0.75i -Y1.0i -P -K > $psfile 

# Add the Coastline and National Boundaries
# 
pscoast -K -O -J -R -B -N1 -N2 -W -Dl -A41 -G250/250/200  >> $psfile 

# Add station locations.  
# Input are longitude latitude.
#
psxy -K -O -J -R -St0.25i -G0/0/0 <<EOF >> $psfile 
-105.044 19.500 
-110.309 24.101 
-106.426 23.184 
EOF

# Add event locations.
# Input are longitude latitude.
#
psxy -O -K -J -R -W10/0/0/0  -Sc0.25i  <<EOF >> $psfile 
-108.110 22.348 
EOF

# End the Postscript File
# 
psxy -R -J -O /dev/null >> $psfile 

