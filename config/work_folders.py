import os

from exceptions.exceptions import DirectoryAlreadyExistException


def make_dir(in_path, out_path):
    if out_path not in [file.path for file in os.scandir(os.path.dirname(in_path))]:
        os.makedirs(out_path)
    else:
        raise DirectoryAlreadyExistException()

    return [in_path, out_path]


def remove_dir(path):
    os.rmdir(path)
