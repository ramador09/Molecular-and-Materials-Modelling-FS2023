#!/bin/bash
#SBATCH --no-requeue
#SBATCH --job-name="h2o"
#SBATCH --get-user-env
#SBATCH --output=_scheduler-stdout.txt
#SBATCH --error=_scheduler-stderr.txt
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=12
#SBATCH --cpus-per-task=1
#SBATCH --time=04:00:00


### computer prepend_text start ###
#SBATCH --partition=normal
#SBATCH --account=s1141
#SBATCH --constraint=gpu
#SBATCH --hint=nomultithread
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export CRAY_CUDA_MPS=1
ulimit -s unlimited
### computer prepend_text end ###


module load daint-mc
module load CP2K


'srun' '-n' '24' '/apps/dom/UES/jenkins/7.0.UP03/21.09/dom-mc/software/CP2K/9.1-CrayGNU-21.09/bin/cp2k.psmp' '-i' 'h2o.inp'  > 'h2o.out' 2>&1

 

 
