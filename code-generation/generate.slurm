#!/bin/bash
# ---------------------------------------------------------------------
# Script to process any file for temporary work
# ---------------------------------------------------------------------
#SBATCH --job-name=temp-run
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=128gb
#SBATCH --time=0-24:00:00
#SBATCH --partition=bigmem

#SBATCH --partition=gpu-a100
#SBATCH --gres=gpu:2  # Request 2 GPUs
# ---------------------------------------------------------------------
echo "Starting run at: `date`"
# ---------------------------------------------------------------------
# module load python/3.9.7
source ~/software/init-conda
conda activate myenv
python generate.py --model_name codeparrot/codeparrot --path data/TheVault
# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: `date`"
# ---------------------------------------------------------------------


# USAGE:
# $sbatch your-file.slum
# $squeue -u your_username
# $squeue -j jobID
# $scontrol show job jobID
# $squeue -p partition_name

# current_id: squeue -j 31751380, 31754126