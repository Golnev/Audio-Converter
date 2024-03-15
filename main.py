import argparse
import os

from config.find_folder import out_folder, len_folder, find_folder
from exceptions.exceptions import DirectoryAlreadyExistException
import logger.logging_config as log
from config.work_folders import make_dir
from src.convert import converter


def main():
    parser = argparse.ArgumentParser(description='Audio Converter')
    parser.add_argument('--input_format', '-inp', help='Enter what format to convert from.')
    parser.add_argument('--output_format', '-out', help='Enter what format to convert to.')
    parser.add_argument('--from_directory', '-fd', help='Enter the directory to convert from.')
    args = parser.parse_args()

    if args.from_directory:
        input_path = args.from_directory
        output_path = out_folder(input_path)
        file_len = len_folder(input_path)
        make_dir(input_path, output_path)
    else:
        try:
            input_path = find_folder()
            output_path = out_folder(input_path)
            file_len = len_folder(input_path)
            make_dir(input_path, output_path)
        except DirectoryAlreadyExistException as e:
            log.directory_already_exist_log(os.path.basename(output_path), e.message)
            return

    if not args.input_format:
        args.input_format = input('Enter input format: ')

    if not args.output_format:
        args.output_format = input('Enter output format: ')

    converter(input_path, output_path, args.input_format, args.output_format, file_len)


if __name__ == '__main__':
    log.logger.info('Start app.')
    main()
    log.logger.info('Finish app.')
