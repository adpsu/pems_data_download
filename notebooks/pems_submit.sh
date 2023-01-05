#!/bin/bash
#SBATCH --job-name=PEMS_JOB_DIST_4_2021
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=amd7293@psu.edu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=198gb
#SBATCH --time=08:00:00
#SBATCH --output=PEMS_JOB_DIST_%j.log
cd $SLURM_SUBMIT_DIR
source ~/.bashrc
module purge
module load anaconda3
conda activate pems
python3 pems_data_downloader.py --user_id 'amd7293@psu.edu' --password 'A09381g@0027' --district 4 --start_year 2021 --end_year 2021 --file_type 'station_5min'
