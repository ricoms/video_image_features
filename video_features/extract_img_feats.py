import numpy as np
import os
from tqdm import tqdm
import cv2
import PIL.Image as Image
from PIL import ImageFile
import multiprocessing
from joblib import Parallel, delayed

import __folder_params
import input_data

import sys
sys.path.insert(0, __folder_params.home)
import utils

sys.path.insert(0, __folder_params.home + 'image_features/')
import color_histogram
import hog
import inceptionV3
import lbp
import orb

ImageFile.LOAD_TRUNCATED_IMAGES = True

def get_frames_data(filename, num_frames_per_clip=3):
    ''' Given a directory containing extracted frames, return a video clip of
    (num_frames_per_clip) consecutive frames as a list of np arrays '''
    cap = cv2.VideoCapture(filename)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))
    ret_arr = []
    frames = []
    fc = 0
    ret = True
    division = frameCount // num_frames_per_clip
    for i in range(frameCount):
        ret, buf[i] = cap.read()
        if i % division == 0:
            ret_arr.append(buf[i])
            frames.append(i)
    cap.release()
    return ret_arr, frames


def run():
    n_tot = sum(1 for _ in utils.get_files_iterator('video'))
    video_iterator = utils.get_files_iterator('video')
    num_cores = multiprocessing.cpu_count()

    img_funcs =\
    {
        'ColorHistogram': color_histogram.processHistogram,
        'Hog': hog.processHog,
        'LBP': lbp.processLBP,
        'ORB': orb.processOrb
    }
    bath_img_funcs =\
    {
        'InceptionV3imagenet': inceptionV3.processDnn
    }
    imgs_batches = []
    for video_path in tqdm(video_iterator, total=n_tot):

        ret_arr, frames = get_frames_data(video_path)

        batch = []
        for i, frame in enumerate(ret_arr):
            img = Image.fromarray(frame, 'RGB')
            temp_img_path = video_path.replace('.webm', '-{}.png'.format(frames[i]))
            if not os.path.exists(temp_img_path):
                img.save(temp_img_path)
            batch.append(temp_img_path)


        #for k, func in img_funcs.items():
            #Parallel(n_jobs=num_cores, verbose=0)(
                #delayed(func)(path_to_file) for path_to_file in batch)
        imgs_batches.append(batch)

    for batch in tqdm(imgs_batches, total=len(imgs_batches)):

        inceptionV3.processDnn(batch)

        for img_path in batch:
            os.remove(img_path)


if __name__ == "__main__":
    run()
