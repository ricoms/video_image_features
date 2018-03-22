import __folder_params

import sys
sys.path.insert(0, __folder_params.home)
import utils
from extract_features import FeatureExtractor

from skimage import exposure
import cv2

def processHistogram(img_path, radius = 15):
    """ Extracts histogram for each color channel. """
    img = cv2.imread(img_path)
    final_path = utils.adress_file(img_path, "ColorHistogram")

    # http://scikit-image.org/docs/dev/api/skimage.exposure.html#skimage.exposure.histogram
    R, G, B = img[:, :, 2], img[:, :, 1], img[:, :, 0]
    Rhistogram = exposure.histogram(R)
    Ghistogram = exposure.histogram(G)
    Bhistogram = exposure.histogram(B)

    with open(final_path, 'w+') as f:
        for histogram in (Rhistogram, Ghistogram, Bhistogram):
            values, bins = histogram
            for v, b in zip(values, bins):
                f.write("%d:%d " % (b, v))
            f.write("\n")

if __name__ == "__main__":
    FeatureExtractor("image", processHistogram).run()
    #a = FeatureExtractor("image", processHistogram)
    #print(next(a.data_iterator))
    #processHistogram(next(a.data_iterator))
