import __folder_params

import sys
sys.path.insert(0, __folder_params.home)
import utils
from extract_features import FeatureExtractor

from keras.applications import InceptionV3
from keras.models import Sequential
from skimage.transform import resize
import skimage.io as skio
import numpy as np
from tqdm import tqdm

def get_inceptionV3():
    return InceptionV3(weights='imagenet',
                        include_top=True,
                        input_shape=(227, 227, 3))

def processDnn(batch_img_paths, model, input_shape = (227,227, 3)):
    batch_len = len(batch_img_paths)
    final_paths = []
    for img_path in batch_img_paths:
        final_paths.append(utils.adress_file(img_path, "InceptionV3"))

    X = np.empty((batch_len, *input_shape))
    for i, img_path in enumerate(batch_img_paths):
        img = resize(skio.imread(img_path),
        input_shape, mode='constant', clip = True, preserve_range = True)
        X[i, :, :, :] = img

    out = model.predict(X)

    for i, pred in enumerate(out):
        with open(final_paths[i], 'w+') as f:
            for i, v in enumerate(pred):
                if v > 0:
                    f.write("%d:%e " % (i, v))

if __name__ == "__main__":
    #FeatureExtractor("image", processInceptionV3).run()
    a = FeatureExtractor("image", processDnn)
    images_paths = [i for i in a.data_iterator]
    batch = 32

    batches = []
    for i in range(len(images_paths)//32):
        batches.append(images_paths[i*32:(i+1)*32])
    batches.append(images_paths[(i+1)*32:])
    model = get_inceptionV3()

    for img_batch in tqdm(batches, total=len(batches)):
        processDnn(img_batch, model)
