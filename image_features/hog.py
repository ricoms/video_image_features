import __folder_params

import sys
sys.path.insert(0, __folder_params.home)
import utils
from extract_features import FeatureExtractor

from skimage.feature import hog
from scipy.stats import itemfreq
import cv2

def processHog(img_path, pixels_per_cell=(32, 32), cells_per_block=(1, 1)):
    final_path = utils.adress_file(img_path, "Hog")

    # http://scikit-image.org/docs/dev/api/skimage.feature.html#skimage.feature.hog
    img = cv2.imread(img_path)
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fd = hog(im_gray, block_norm='L2-Hys', cells_per_block=cells_per_block,
            pixels_per_cell = pixels_per_cell)
    # Calculate the histogram
    x = itemfreq(fd.ravel())
    # Normalize the histogram
    hist = x[:, 1]/sum(x[:, 1])

    with open(final_path, 'w+') as f:
        for v in hist:
            f.write("%.8f " % (v))

if __name__ == "__main__":
    FeatureExtractor("image", processHog).run()
    #a = FeatureExtractor("image", processHog)
    #print(next(a.data_iterator))
    #processHog(next(a.data_iterator))
    #processHog(next(a.data_iterator))
