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

for <dist> and <year>

python3 pems_data_downloader.py --user_id 'xyz@psu.edu' --password 'ABCD1234' --district <dist> --start_year <year> --end_year <year> --file_type 'station_5min'

Make sure to change the path where you want to save the csv file(s)

You need to change the .py file if you want different file type.

Available Districts: 

['3', '4', '5', '6', '7', '8', '10', '11', '12']
