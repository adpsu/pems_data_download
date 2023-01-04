#!/bin/bash
dist = 4
year = 2020
#SBATCH --job-name=PEMS_JOB_DIST_$dist_$year
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=amd7293@psu.edu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=64gb
#SBATCH --time=01:00:00
#SBATCH --output=PEMS_JOB_DIST_$dist_$year.log
cd $SLURM_SUBMIT_DIR
source ~/.bashrc
module purge
module load anaconda3
conda activate pems
python3 pems_data_downloader.py --user_id 'amd7293@psu.edu' --password 'A09381g@0027' --district $dist --start_year $year --end_year $year --file_type 'station_5min'
cd /storage/home/amd7293/caltrans-pems/saved_data/
mkdir -p dist_$dist
cd dist_4
mkdir -p $year
cd /storage/home/amd7293/caltrans-pems/data/
mv *$dist* /storage/home/amd7293/caltrans-pems/saved_data/dist_$dist/$year
rm -rf /storage/home/amd7293/caltrans-pems/data/{*,.*}
