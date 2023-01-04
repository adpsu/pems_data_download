# pems_data_download
The main idea is taken from Seb-Good/caltrans-pems:master. I have edited a few things to run it on PSU ICDS cluster (Roar Collab).
Change a few things to make it work: 

Create a conda environment which will have:
numpy==1.18.1
pandas==1.0.3
matplotlib==3.1.3
mechanize==0.4.5
beautifulsoup4==4.9.0
cookiejar==0.0.3

Then edit notebooks/pems_submit.sh 
and edit notebooks/pems_data_downloader.py for "distirct" "Start date" and "End date"
