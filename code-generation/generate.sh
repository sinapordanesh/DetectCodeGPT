#!/bin/bash
# ---------------------------------------------------------------------
# Script to process any file for temporary work on Digital Research Alliance Canada
# ---------------------------------------------------------------------
#SBATCH --job-name=code-generation-run
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --gpus-per-node=a100:2
#SBATCH --mem=256gb
#SBATCH --time=0-110:00:00

# Optional: Email notifications
#SBATCH --mail-user=myhomeqrc@gmail.com
#SBATCH --mail-type=BEGIN,END,FAIL

# ---------------------------------------------------------------------
echo "Starting run at: `date`"
# ---------------------------------------------------------------------
source ../env/bin/activate
python generate.py --path data/CodeSearchNet --model_name codellama/CodeLlama-7b-hf --max_num 100000
# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: `date`"
# ---------------------------------------------------------------------


# current_id: squeue -j 33101314