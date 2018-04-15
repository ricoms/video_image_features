import __folder_params

import sys
sys.path.insert(0, __folder_params.home)
import utils

from skimage.feature import local_binary_pattern
from scipy.stats import itemfreq
import cv2

def processLBP(img_path, radius = 15):
    final_path = utils.adress_file(img_path, "LBP")

    # http://scikit-image.org/docs/dev/api/skimage.feature.html#skimage.feature.local_binary_pattern
    img = cv2.imread(img_path)
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Number of points to be considered as neighbourers
    no_points = 8 * radius
    # Uniform LBP is used
    lbp = local_binary_pattern(im_gray, no_points, radius, method='uniform')
    # Calculate the histogram
    x = itemfreq(lbp.ravel())
    # Normalize the histogram
    hist = x[:, 1]/sum(x[:, 1])

    with open(final_path, 'w+') as f:
        for v in hist:
            f.write("%.8f " % (v))
        f.write("\n")

if __name__ == "__main__":
    utils.FeatureExtractor("image", processLBP).run()
    #a = FeatureExtractor("image", processLBP)
    #print(next(a.data_iterator))
    #processLBP(next(a.data_iterator))
    #processLBP(next(a.data_iterator))
