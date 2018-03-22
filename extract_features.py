
import multiprocessing
from joblib import Parallel, delayed

import utils
import __project_params


class FeatureExtractor:
    def __init__(self, tipo, feat_extract_fn, pre_fn=None):
        self.data_iterator = utils.get_files_iterator(tipo)

        self.feat_fn = feat_extract_fn
        if pre_fn is not None:
            pre_fn()

    def run(self):
        num_cores = multiprocessing.cpu_count()

        Parallel(n_jobs=num_cores, verbose=5)(
            delayed(self.feat_fn)(path_to_file) for path_to_file in self.data_iterator)

if __name__ == "__main__":
    data_iterator = utils.get_files_iterator("video")
    a = [i for i in data_iterator]
    print(len(a))
