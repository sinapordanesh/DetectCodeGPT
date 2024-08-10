#!/bin/bash
# ---------------------------------------------------------------------
# Script to process any file for temporary work
# ---------------------------------------------------------------------
#SBATCH --job-name=temp-run
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32gb
#SBATCH --time=0-2:00:00
#SBATCH --partition=bigmem

#SBATCH --partition=gpu-a100
#SBATCH --gres=gpu:1  # Request 1 GPU
# ---------------------------------------------------------------------
echo "Starting run at: `date`"
# ---------------------------------------------------------------------
# module load python/3.9.7
source ~/software/init-conda
conda activate myenv
python 1.analyze_length.py
# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: `date`"
# ---------------------------------------------------------------------


# USAGE:
# $sbatch your-file.slum
# $squeue -u your_username
# $squeue -j jobID
# $scontrol show job jobID
# $squeue -p partition_name

# current_id: squeue -j 31550134