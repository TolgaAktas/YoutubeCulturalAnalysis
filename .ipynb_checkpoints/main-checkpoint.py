{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import h5py\n",
    "import glob \n",
    "import os\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def removeDuplicates(thumbnail):\n",
    "    \n",
    "    seen_labels = []\n",
    "    \n",
    "    boxes = thumbnail[\"boxes\"]\n",
    "    scores= thumbnail[\"scores\"]\n",
    "    labels= thumbnail[\"labels\"]\n",
    "    \n",
    "    new_boxes = np.copy(boxes)\n",
    "    new_scores= np.copy(scores)\n",
    "    new_labels= np.array(labels)\n",
    "    \n",
    "    for idx,label in enumerate(labels):\n",
    "        \n",
    "        if label in seen_labels:\n",
    "            np.delete(new_boxes,idx,axis=0)\n",
    "            np.delete(new_labels,idx,axis=0)\n",
    "            np.delete(new_scores,idx,axis=0)\n",
    "        else:\n",
    "            seen_labels.append(label)\n",
    "    \n",
    "    return {\"boxes\":new_boxes,\"scores\":new_scores,\"labels\":new_labels}  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "all the input arrays must have same number of dimensions",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-19-ee9db63b015b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     34\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     35\u001b[0m             \u001b[0mall_thumbnails\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mone_thumbnail\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 36\u001b[1;33m             \u001b[0mreduced_thumbnails\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mremoveDuplicates\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mone_thumbnail\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     37\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     38\u001b[0m             \u001b[0mdset\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mclass_name\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mall_thumbnails\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-18-7991be2207fd>\u001b[0m in \u001b[0;36mremoveDuplicates\u001b[1;34m(thumbnail)\u001b[0m\n\u001b[0;32m     15\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mlabel\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mseen_labels\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     16\u001b[0m             \u001b[0mseen_labels\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlabel\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 17\u001b[1;33m             \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnew_boxes\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mboxes\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0midx\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     18\u001b[0m             \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnew_scores\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mscores\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0midx\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     19\u001b[0m             \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnew_labels\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mlabel\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\numpy\\lib\\function_base.py\u001b[0m in \u001b[0;36mappend\u001b[1;34m(arr, values, axis)\u001b[0m\n\u001b[0;32m   4692\u001b[0m         \u001b[0mvalues\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mravel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4693\u001b[0m         \u001b[0maxis\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0marr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mndim\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 4694\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mconcatenate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0marr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalues\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   4695\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4696\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: all the input arrays must have same number of dimensions"
     ]
    }
   ],
   "source": [
    "COCO_INSTANCE_CATEGORY_NAMES = [\n",
    "    '_background_', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',\n",
    "    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',\n",
    "    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',\n",
    "    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',\n",
    "    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',\n",
    "    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',\n",
    "    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',\n",
    "    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',\n",
    "    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',\n",
    "    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',\n",
    "    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',\n",
    "    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'\n",
    "]\n",
    "\n",
    "dict_keys = ['CA','DE','FR','GB','IN','JP','KR','MX','RU','US']\n",
    "dset = {}\n",
    "reduced_dset = {}\n",
    "\n",
    "for f in glob.glob('data/*.{}'.format('h5')):\n",
    "    with h5py.File(f, 'r') as h5_file: \n",
    "        \n",
    "        class_name = os.path.splitext(os.path.basename(f))[0]\n",
    "        all_thumbnails = []\n",
    "        reduced_thumbnails = []\n",
    "        \n",
    "        for key in h5_file.keys():\n",
    "            \n",
    "            boxes = h5_file[key]['boxes'][:]\n",
    "            scores = h5_file[key]['scores'][:]\n",
    "            labels = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in h5_file[key]['labels'][:]]\n",
    "            \n",
    "            one_thumbnail = {\"boxes\":boxes,\"scores\":scores,\"labels\":labels}\n",
    "            \n",
    "            all_thumbnails.append(one_thumbnail)\n",
    "            reduced_thumbnails.append(removeDuplicates(one_thumbnail))\n",
    "            \n",
    "            dset[class_name] = all_thumbnails\n",
    "            reduced_dset[class_name] = reduced_thumbnails"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(29,)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reduced_dset[\"CA\"][14]['labels'].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "29"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(dset[\"CA\"][14][\"labels\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "reduced_dset[\"CA\"][1235][\"labels\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dset['CA'][235]['scores'].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
