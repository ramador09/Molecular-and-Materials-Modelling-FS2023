#!/bin/bash -l
#
# CP2K on Piz Daint: 1 node, 1 MPI task per node, 12 OpenMP threads per task
#
#SBATCH --job-name="mol. dyn."
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --account=crs01
#SBATCH --partition=normal
#SBATCH --ntasks-per-node=12
#SBATCH --cpus-per-task=1
#SBATCH --constraint=gpu
#========================================
# load modules and run simulation

module load daint-gpu
module load CP2K
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
export CRAY_CUDA_MPS=1
ulimit -s unlimited
srun -n 12 cp2k.popt -i md.inp -o md.out
