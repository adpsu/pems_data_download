# Import 3rd party libraries
import os
import sys
import pandas as pd
import glob
import argparse
import calendar

# Local imports
sys.path.insert(0, os.path.dirname(os.path.abspath(os.getcwd())))
from pems.handler import PeMSHandler

# Configure Notebook
import warnings
warnings.filterwarnings('ignore')
#%matplotlib inline
#%load_ext autoreload
#%autoreload 2

parser = argparse.ArgumentParser()
parser.add_argument(
    '--user_id',
    help='your CalTrans PeMs user id',
    default='xyz@psu.edu',
    type=str)
parser.add_argument(
    '--password',
    help='your CalTrans PeMs password',
    default='abc123',
    type=str)
parser.add_argument(
    '--district',
    help='Select a district',
    default=3,
    type=str)
parser.add_argument(
    '--start_year',
    help='Start year of data collection',
    default=2020,
    type=int)
parser.add_argument(
    '--end_year',
    help='End year of data collection',
    default=2020,
    type=int)
parser.add_argument(
    '--file_type',
    help='Enter file type',
    default='station_5min',
    type=str)

args = parser.parse_args()
user = args.user_id
pswd = args.password
dist = args.district
start = args.start_year
end =  args.end_year
file = args.file_type


# Connect to PeMS
pems = PeMSHandler(username=user, password=pswd)

# View labels reference
pems.label_reference

# View for available file types
pems.get_file_types()

# View for available districts for a file type
pems.get_districts(file_type='station_5min')

months =['January','February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months:
    # View summary of available files for (start_year, end_year, districts, file_types) query
    files = pems.get_files(start_year=start, end_year=end, districts=[dist], file_types=[file], months=None)
    # Download files for (start_year, end_year, districts, file_types) query
    pems.download_files(start_year= start, end_year=end, districts=[dist], file_types=[file], months = [month])

    path = r'/storage/work/amd7293/caltrans-pems/data/' # use your path
    all_files = glob.glob(os.path.join(path , "*.gz"))
    
    for csv in glob.iglob(os.path.join(path, '*.csv')):
        os.remove(csv)
    

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, compression='gzip', header= None, sep=',', quotechar='"')
        li.append(df)
        os.remove(filename)
        
        

    traffic_station_df = pd.concat(li, axis=0, ignore_index=True)

    print('File combined succesfully')

    columns = ["timestamp", "id" ,"district", "freeway_no", "direction", "lane_type", "station_length", "samples", "pct_obs", "total_flow",
          "avg_occ", "avg_speed"]
    #traffic_station_df = pd.read_csv('/storage/home/amd7293/caltrans-pems/data/d03_text_station_5min_2019_02_12.txt.gz',
                                 #compression='gzip', header= None, sep=',', quotechar='"')
    traffic_station_df = traffic_station_df.iloc[:, 0:12]
    traffic_station_df.columns = columns

    traffic_station_df.to_pickle('/storage/work/amd7293/caltrans-pems/CSV/traffic_station_df_dist_'+str(dist)+'_'+str(start)+'_month_'+str(month)+'.pkl',compression='gzip')
    print('File saved succesfully for month: '+str(month))

