#!/bin/bash
USER=comcon1
EPORT=8889
set echo off

cat << EOF

You !!MUST!! cite the following paper:

 Briggs, J. A., Weinreb, C., Wagner, D. E., Megason, S., Peshkin, L., 
 Kirschner, M. W., & Klein, A. M. (2018). The dynamics of gene expression 
 in vertebrate embryogenesis at single-cell resolution. Science, 360(6392), eaar5780.

All the data in the container were obtained from the public repository:

 https://kleintools.hms.harvard.edu/tools/currentDatasetsList_xenopus_v2.html

EOF

docker run \
    --name xenopus-jamboree \
    -d \
    -p${EPORT}:8888 \
    -v $PWD/work:/home/jovyan/work \
    ${USER}/xjbr

cat << EOF

Wait 10 sec until jupyter starts..

EOF

sleep 10 

docker exec xenopus-jamboree jupyter notebook list

