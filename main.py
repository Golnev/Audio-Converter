import os

from config.find_folder import out_folder, len_folder, find_folder
from exceptions.exceptions import DirectoryAlreadyExistException
import logger.logging_config as log
from config.work_folders import make_dir
from src.convert import converter
from src.parser import parse_arguments


def main():
    args = parse_arguments()

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
