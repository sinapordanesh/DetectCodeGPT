#!/bin/bash
# ---------------------------------------------------------------------
# Script to process any file for temporary work
# ---------------------------------------------------------------------
#SBATCH --job-name=temp-run
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=256gb
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
python generate.py --path data/CodeSearchNet/splitted/train_5 --model_name codellama/CodeLlama-7b-hf --max_num 20000
# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: `date`"
# ---------------------------------------------------------------------


# USAGE:
# $sbatch your-file.slum
# $squeue -u your_username
# $squeue -j jobID
# $scontrol show job jobID
# $squeue -p partition_name

# current_id: squeue -j 31847603, 31847833, 31847843, 31847846, 31847848