#!/bin/bash
#
#SBATCH --job-name=tar_new_laoe_data
#SBATCH --output=tar_new_laoe.txt
#
#SBATCH --account=vnarsim
#SBATCH --ntasks=2
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=100

tar --create --file /scratch/halstead/l/lin891/laoe_new_partial.tar.gz --gzip /scratch/halstead/l/lin891/laoe_new/
rsync /scratch/halstead/l/lin891/laoe_new_partial.tar.gz /depot/vnarsim/data/lin_data/ 
