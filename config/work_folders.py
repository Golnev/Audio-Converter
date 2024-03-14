import os

from exceptions.exceptions import DirectoryAlreadyExistException
from config.find_folder import find_folder

input_path = find_folder()
output_path = f'{os.path.dirname(input_path)}\\{os.path.basename(input_path)}_MP3'
file_len = len([file for file in os.scandir(input_path) if file.is_file()])


def make_dir(in_path, out_path):
    if out_path not in [file.path for file in os.scandir(os.path.dirname(in_path))]:
        os.makedirs(out_path)
    else:
        raise DirectoryAlreadyExistException()


def remove_dir(path):
    os.rmdir(path)
