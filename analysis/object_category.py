files = ['data/CAvideos.csv','data/USvideos.csv','data/INvideos.csv','data/FRvideos.csv','data/DEvideos.csv',
         'data/RUvideos.csv','data/MXvideos.csv','data/GBvideos.csv','data/JPvideos.csv','data/KRvideos.csv']
import glob
import pandas as pd
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

# import json
# all_ids = []
# id_files = ['data/CA_category_id.json','data/US_category_id.json','data/IN_category_id.json','data/FR_category_id.json','data/DE_category_id.json',
#             'data/RU_category_id.json','data/MX_category_id.json','data/GB_category_id.json','data/JP_category_id.json','data/KR_category_id.json']
# for file in id_files:
#     ids = [item['id'] for item in json.load(open(file))['items']]
#     category_titles = [item['snippet']['title'] for item in json.load(open(file))['items']]
#     print(category_titles)
ids = [1, 2, 10, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
category_titles = ['Film & Animation', 'Autos & Vehicles', 'Music', 'Pets & Animals', 'Sports', 'Short Movies', 'Travel & Events',
                   'Gaming', 'Videoblogging', 'People & Blogs', 'Comedy', 'Entertainment', 'News & Politics', 'Howto & Style',
                   'Education', 'Science & Technology', 'Movies', 'Anime/Animation', 'Action/Adventure', 'Classics', 'Comedy',
                   'Documentary', 'Drama', 'Family', 'Foreign', 'Horror', 'Sci-Fi/Fantasy', 'Thriller', 'Shorts', 'Shows', 'Trailers']

COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]
valid_object_idxs = []
for i, name in enumerate(COCO_INSTANCE_CATEGORY_NAMES):
    if name in ['N/A','__background__']:
        continue
    else:
        valid_object_idxs.append(i)
valid_object_names = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in valid_object_idxs]

import h5py
import numpy as np
vids = []
# for f in glob.glob('data/*.{}'.format('h5')):
for f in ['data/US.h5']:
    country = f[5:7]
    category_counts = [0 for _ in ids]
    with h5py.File(f, 'r') as h5_file:
        object_category_map = np.zeros((91, len(ids)))
        for vid in h5_file.keys():
            if vid == 'v_#NAME?':
                continue
            vids.append(vid[2:])
            if vid[2:] not in my_df.index:
                continue
            category_id = my_df.loc[vid[2:]]['category_id']
            if category_id not in ids:
                continue
            col_idx = ids.index(category_id)
            category_counts[col_idx] += 1
            labels = np.unique(h5_file[vid]['labels'][:]).tolist()
            for l in labels:
                object_category_map[l,col_idx] += 1
    print(country, category_counts)

    for col_idx, count in enumerate(category_counts):
        if count > 0:
            object_category_map[:,col_idx] /= count

    object_category_map = object_category_map[valid_object_idxs].transpose()

    import matplotlib.pyplot as plt
    from matplotlib import cm
    fig, ax = plt.subplots(figsize=(16,8))
    heatmap = ax.imshow(object_category_map, interpolation='nearest', cmap=cm.OrRd)

    # making the colorbar on the side
    cbar_min = object_category_map.min().min()
    cbar_max = object_category_map.max().max()
    cbar = fig.colorbar(heatmap, ticks=[cbar_min, cbar_max])

    #print labels
    ax.set_yticks(np.arange(len(category_titles)))
    ax.set_xticks(np.arange(len(valid_object_names)))
    ax.set_yticklabels(category_titles, fontsize=9)
    ax.set_xticklabels(valid_object_names, fontsize=9, rotation=90)
    plt.savefig('figures/obj_genre_{}.pdf'.format(country))
    np.save('obj_genre_{}'.format(country), object_category_map)
