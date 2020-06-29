#!/bin/bash
#
#SBATCH --job-name=rsync_aoe_c2e_data
#SBATCH --output=rsync_laoe_c2e.txt
#
#SBATCH --account=vnarsim
#SBATCH --ntasks=1
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=100

SCRATCH_DIR="/scratch/halstead/l/lin891/laoe_c2e/"
DEPOT_DIR="/depot/vnarsim/data/lin_data/laoe_c2e_cont/"

rsync --recursive ${SCRATCH_DIR}* ${DEPOT_DIR}
if [ "$?" -eq "0" ]
then
    rm -r ${SCRATCH_DIR}
    echo "Done and removed scratch files"
else
    echo "Error while running rsync"
fi
