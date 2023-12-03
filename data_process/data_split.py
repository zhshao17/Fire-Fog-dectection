import os
import random
import shutil
import numpy as np
 
def get_imglist(path):
    path = path + '/images'
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
 
def get_txtlist(path):
    path = path + '/labels'
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.txt')]
     
def getData(src_path):
    # dest_dir = src_path  # 这个文件夹需要提前建好
    dest_dir = './Fog'
    img_list = get_imglist(src_path)
    txt_list = get_txtlist(src_path)
    
    shuffled_indices = np.random.permutation(len(img_list))
    test_set_size = int(len(img_list) * 0.1)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    for i in test_indices:
        shutil.copy(img_list[i], dest_dir + '/val/images')
        shutil.copy(txt_list[i], dest_dir + '/val/labels')
    for j in train_indices:
        shutil.copy(img_list[j], dest_dir + '/train/images')
        shutil.copy(txt_list[j], dest_dir + '/train/labels')
        
        
np.random.seed(123)
# nowpath = os.path.realpath(os.curdir)
# path = os.path.join(nowpath, 'Fire\\')
# getData("./Fire")
getData("./data")