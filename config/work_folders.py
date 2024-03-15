import os

from exceptions.exceptions import DirectoryAlreadyExistException
from config.find_folder import find_folder, out_folder, len_folder


def make_dir(in_path, out_path):
    # in_path = find_folder()
    # out_path = out_folder(in_path)
    # f_len = len_folder(in_path)

    if out_path not in [file.path for file in os.scandir(os.path.dirname(in_path))]:
        os.makedirs(out_path)
    else:
        raise DirectoryAlreadyExistException()

    return [in_path, out_path]


def remove_dir(path):
    os.rmdir(path)
