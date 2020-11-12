#!/bin/bash
#
#SBATCH --job-name=rsync_job
#SBATCH --output=rsync_job.txt
#
#SBATCH --account=vnarsim
#SBATCH --ntasks=1
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=8192

SCRATCH_DIR="/scratch/brown/lin891/os_shear/"
DEPOT_DIR="/depot/vnarsim/data/lin_data/os_shear/"

rsync --recursive ${SCRATCH_DIR}* ${DEPOT_DIR}
if [ "$?" -eq "0" ]
then
    rm -r ${SCRATCH_DIR}
    echo "Done and removed scratch files"
else
    echo "Error while running rsync"
fi
