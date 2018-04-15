import __folder_params

import sys
sys.path.insert(0, __folder_params.home)
import utils

import subprocess

def extract_sounds_from_vids():
    ivid = utils.get_files_iterator('video')
    for v in ivid:
        cm = 'ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {}'.format(
            v, v.replace('.webm', '.wav'))
        subprocess.call(cm, shell=True)
    sound_it = utils.get_files_iterator(end='wav')
    return isound

if __name__ == "__main__":
    a = utils.get_files_iterator(None, 'wav')
    print(len([s for s in a]))
    #print(len([s for s in extract_sounds_from_vids()]))
