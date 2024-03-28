#!/bin/bash -l
#SBATCH --time=6:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:2
#SBATCH --mem=50G  
#SBATCH --partition=alpha
ml release/23.04 GCC/11.3.0 OpenMPI/4.1.4 CUDA/11.7.0 Python/3.10 ImageMagick/7.1.0-37
python unet_train.py  
 
