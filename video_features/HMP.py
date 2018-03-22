import __folder_params

import sys
sys.path.insert(0, __folder_params.home)
import utils
from extract_features import FeatureExtractor

import subprocess
import os

def make_source():
    """ Runs make command on c scripts. """
    PathToLaunch = sys.path[1]+'/sources/vir/'
    origWD = os.getcwd() # remember our original working directory
    os.chdir(PathToLaunch)
    command = 'make clean '
    subprocess.run(command, shell=True)
    command = 'make video2signature '
    subprocess.run(command, shell=True)
    command = 'make histogram2libsvm '
    subprocess.run(command, shell=True)
    os.chdir(origWD) # get back to our original working directory

def processHmps(video_path):
    """ Extract the hmp feat and turn binary (hmp) file into txt. """
    final_path = utils.adress_file(video_path, "HMP")
    hmp_path = final_path.replace('.txt', '.hmp')

    cm = sys.path[1]+'/sources/vir/./video2signature -srate 3 {0} > {1}'.format(
        video_path, hmp_path)
    subprocess.run(cm, shell=True)
    cm = sys.path[1]+'/sources/vir/./histogram2libsvm {0} > {1}'.format(
        hmp_path, final_path)
    subprocess.run(cm, shell=True)

    os.remove(hmp_path)

if __name__ == "__main__":

    FeatureExtractor("video", processHmps, make_source).run()
