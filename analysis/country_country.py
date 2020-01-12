files = ['data/CAvideos.csv','data/USvideos.csv','data/INvideos.csv','data/FRvideos.csv','data/DEvideos.csv',
         'data/RUvideos.csv','data/MXvideos.csv','data/GBvideos.csv','data/JPvideos.csv','data/KRvideos.csv']
import glob
import pandas as pd
from tqdm import tqdm
import numpy as np

dfs = list()
for csv in files:
    df = pd.read_csv(csv, index_col='video_id', encoding = "ISO-8859-1")
    df['country'] = csv[5:7]
    dfs.append(df)

my_df = pd.concat(dfs)
my_df.head(3)

my_df['trending_date'] = pd.to_datetime(my_df['trending_date'],errors='coerce', format='%y.%d.%m')
my_df['publish_time'] = pd.to_datetime(my_df['publish_time'], errors='coerce', format='%Y-%m-%dT%H:%M:%S.%fZ')

my_df = my_df[my_df['trending_date'].notnull()]
my_df = my_df[my_df['publish_time'].notnull()]
my_df = my_df[my_df.index != '#NAME?']

my_df = my_df.dropna(how='any',inplace=False, axis = 0)

my_df.insert(4, 'publish_date', my_df['publish_time'].dt.date)
my_df['publish_time'] = my_df['publish_time'].dt.time

my_df_full = my_df.reset_index().sort_values('trending_date').set_index('video_id')
my_df = my_df.reset_index().sort_values('trending_date').drop_duplicates('video_id',keep='last').set_index('video_id')
my_df[['publish_date','publish_time']].head()

import h5py
vids = []
labels = {}
for f in glob.glob('data/*.{}'.format('h5')):
    with h5py.File(f, 'r') as h5_file:
        for vid in h5_file.keys():
            vids.append(vid[2:])
my_df = my_df.loc[vids]
my_df = my_df.reset_index().sort_values('trending_date').drop_duplicates('video_id',keep='last').set_index('video_id')

fre_df = pd.DataFrame(my_df_full.groupby([my_df_full.index,'country']).count()['title'].sort_values(ascending=False)).reset_index()

corr_list = pd.DataFrame(fre_df['video_id'].unique(), columns=['video_id'])
for country_code in fre_df['country'].unique():
    corr_list[country_code] = 0
corr_list['total']=0
corr_list=corr_list.set_index('video_id')
#print new_list

pbar = tqdm(total=len(corr_list))
for idx, (index , item) in enumerate(corr_list.iterrows()):#corr_list.iterrows()
    #print index
    total = 0
    for i ,row in fre_df[fre_df['video_id'] == index][['country','title']].iterrows():
        total += row['title']
        corr_list.loc[[index],[row['country']]] = row['title']
    corr_list.loc[[index],['total']] = total
    pbar.update(1)
pbar.close()
corr_list.head()

countries = ['GB', 'US', 'CA', 'DE', 'FR', 'IN', 'MX', 'RU', 'JP', 'KR'] #looking at correlations between these countries
corr_matrix = corr_list[countries].corr()

import matplotlib.pyplot as plt
from matplotlib import cm
fig, ax = plt.subplots(figsize=(15,15))
fig.suptitle('Correlation between countries', fontsize=20).set_y(0.85)
heatmap = ax.imshow(corr_matrix, interpolation='nearest', cmap=cm.OrRd)

# making the colorbar on the side
cbar_min = corr_matrix.min().min()
cbar_max = corr_matrix.max().max()
cbar = fig.colorbar(heatmap, ticks=[cbar_min, cbar_max])

# making the labels
labels = ['']
for column in countries:
    labels.append(column)
#print labels
ax.set_yticks(np.arange(len(labels)))
ax.set_xticks(np.arange(len(labels)))
ax.set_yticklabels(labels, minor=False, fontsize=15)
ax.set_xticklabels(labels, minor=False, fontsize=15)
plt.savefig('figures/heatmap.png')
corr_matrix.to_csv('country_country_corr.csv')
