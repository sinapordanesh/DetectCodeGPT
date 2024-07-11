#!/bin/bash
# ---------------------------------------------------------------------
# Script to process any file for temporary work
# ---------------------------------------------------------------------
#SBATCH --job-name=temp-run
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64gb
#SBATCH --time=0-24:00:00
#SBATCH --partition=bigmem
# ---------------------------------------------------------------------
echo "Starting run at: `date`"
# ---------------------------------------------------------------------
# module load python/3.9.7
source ~/software/init-conda
conda activate myenv
python generate.py
# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: `date`"
# ---------------------------------------------------------------------


# USAGE:
# $sbatch your-file.slum
# $squeue -u your_username
# $squeue -j jobID
# $scontrol show job jobID
# $squeue -p partition_name

# current_id: 31320653