import __folder_params

import sys
sys.path.insert(0, __folder_params.home)
import utils
from extract_features import FeatureExtractor
import data_handler

from skimage.feature import ORB
from scipy.stats import itemfreq
import cv2
import pickle

def processOrb(img_path):

    final_path = utils.adress_file(img_path, "ORB", end='.p')
    # http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_orb/py_orb.html
    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints with ORB
    img = cv2.imread(img_path)
    kp = orb.detect(img, None)

    # compute the descriptors with ORB
    keypoints, descriptors = orb.compute(img, kp)

    temp = data_handler.pickle_keypoints(keypoints, descriptors)

    pickle.dump(temp, open(final_path, "wb"))

if __name__ == "__main__":
    FeatureExtractor("image", processOrb).run()
    #a = FeatureExtractor("image", processOrb)
    #print(next(a.data_iterator))
    #processOrb(next(a.data_iterator))
    #processOrb(next(a.data_iterator))
