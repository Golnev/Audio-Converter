from pydub import AudioSegment
import os

from exceptions.exceptions import DirectoryAlreadyExistException, FormatException
import logger.logging_config as log
from config.work_folders import input_path, output_path, file_len, make_dir
from src.convert import converter


def main():
    # input_folder = input_path
    # output_folder = output_path

    try:
        make_dir(input_path, output_path)
    except DirectoryAlreadyExistException as e:
        log.directory_already_exist_log(os.path.basename(output_path), e.message)
        return

    converter(input_path, output_path, 'flac', 'mp3', file_len)


if __name__ == '__main__':
    log.logger.info('Start app.')
    main()
    log.logger.info('Finish app.')
