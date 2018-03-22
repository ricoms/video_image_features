import os
import re
import glob

import __project_params

def get_files_iterator(tipo):
    """ Returns iterator of files of tipo (image/video) from the dataset. """
    if tipo == "image":
        return glob.iglob(__project_params.data_folder+'**/*.jpg', recursive=True)
    elif tipo == "video":
        return glob.iglob(__project_params.data_folder+'**/*.webm', recursive=True)
    else:
        raise ValueError('argument must be "image" or "video".')

def create_dir(endereco):
    """ Creates non-existing folders. """
    os.makedirs(os.path.dirname(endereco), exist_ok=True)

def adress_file(original_path, feature, end=".txt"):
    """ Generates a standard file name. """
    path = "/".join(original_path.split("/")[:-1])
    file_name = original_path.split("/")[-1]
    if "images" in path:
        path = path.replace("images", "features/images/"+feature+"/")
        file_name = file_name.replace(".jpg", end)
    else:
        path = re.sub("videos_part[0-9]", "features/videos/"+feature+"/", path)
        file_name = file_name.replace(".webm", end)
    if not os.path.isdir(path):
        create_dir(path)
    final_path = path + file_name
    return final_path

if __name__ == "__main__":
    pass
