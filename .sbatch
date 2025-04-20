#!/bin/bash
#SBATCH -A nr_haml2025
#SBATCH --partition=gpu
#SBATCH --job-name=chirpai-train
#SBATCH --time=03:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=30000
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --qos=normal

module load singularity
singularity run --nv --writable-tmpfs --bind ~/models:/app/models Singularity.sif > ~/log.txt
# https://docs.hpc.kifu.hu/software/singularity.html