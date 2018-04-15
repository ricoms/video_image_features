import os
import re
import glob
import cv2
import numpy as np
import pickle

import __project_params

import multiprocessing
from joblib import Parallel, delayed

class FeatureExtractor:
    def __init__(self, tipo, feat_extract_fn, pre_fn=None):
        self.data_iterator = get_files_iterator(tipo)

        self.feat_fn = feat_extract_fn
        if pre_fn is not None:
            pre_fn()

    def run(self):
        num_cores = multiprocessing.cpu_count()

        Parallel(n_jobs=num_cores, verbose=5)(
            delayed(self.feat_fn)(path_to_file) for path_to_file in self.data_iterator)

def get_files_iterator(tipo=None, end=None):
    """ Returns iterator of files of tipo (image/video) from the dataset. """
    if tipo is not None:
        if tipo == "image":
            return glob.iglob(__project_params.data_folder+'**/*.jpg', recursive=True)
        elif tipo == "video":
            return glob.iglob(__project_params.data_folder+'**/*.webm', recursive=True)
        else:
            raise ValueError('tipo argument must be "image" or "video".')
    if end is not None:
        return glob.iglob(__project_params.data_folder+'**/*.{}'.format(end),
            recursive=True)

def create_dir(endereco):
    """ Creates non-existing folders. """
    os.makedirs(os.path.dirname(endereco), exist_ok=True)

def adress_file(original_path, feature, end=".txt"):
    """ Generates a standard file name. """
    path = "/".join(original_path.split("/")[:-1])
    file_name = original_path.split("/")[-1]
    if "images" in path:
        path = path.replace("images", "features/images/"+feature+"/")
    else:
        path = re.sub("videos_part[0-9]", "features/videos/"+feature+"/", path)
    file_name = '.'.join(file_name.split('.')[:-1]) + end
    if not os.path.isdir(path):
        create_dir(path)
    final_path = path + file_name
    return final_path

def pickle_keypoints(keypoints, descriptors):
    i = 0
    temp_array = []
    for point in keypoints:
        temp = (point.pt, point.size, point.angle, point.response, point.octave,
        point.class_id, descriptors[i])
        ++i
        temp_array.append(temp)
    return temp_array

def unpickle_keypoints(array):
    keypoints = []
    descriptors = []
    for point in array:
        temp_feature = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2], _response=point[3], _octave=point[4], _class_id=point[5])
        temp_descriptor = point[6]
        keypoints.append(temp_feature)
        descriptors.append(temp_descriptor)
    return keypoints, np.array(descriptors)
