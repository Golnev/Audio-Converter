import os

from src.work_dirs.find_folder import out_folder, len_folder, find_folder, find_files, out_folder_from_files
from src.exceptions.exceptions import DirectoryAlreadyExistException
import src.logger.logging_config as log
from src.work_dirs.work_folders import make_dir
from src.convert import Converter
from src.parser import parse_arguments


def main():
    args = parse_arguments()

    if not args.input_format:
        args.input_format = input('Enter input format: ')

    if not args.output_format:
        args.output_format = input('Enter output format: ')

    converter = Converter()

    if args.from_directory and args.from_directory != 'window':
        input_path = args.from_directory
        output_path = out_folder(input_path)
        file_len = len_folder(input_path)
        try:
            make_dir(input_path, output_path)
        except DirectoryAlreadyExistException as e:
            log.directory_already_exist_log(os.path.basename(output_path), e.message)
            return
        converter.convert_from_dir(input_path, output_path, args.input_format, args.output_format, file_len)
    else:
        input_path = find_folder()
        output_path = out_folder(input_path)
        file_len = len_folder(input_path)
        try:
            make_dir(input_path, output_path)
        except DirectoryAlreadyExistException as e:
            log.directory_already_exist_log(os.path.basename(output_path), e.message)
            return
        converter.convert_from_dir(input_path, output_path, args.input_format, args.output_format, file_len)

    if args.path_files and args.path_files != 'window':
        input_files = (args.path_files, )
        output_path = out_folder_from_files(input_files)
        count_files = len(input_files)
        converter.convert_files(input_files, output_path, args.input_format, args.output_format, count_files)
    else:
        input_files = find_files()
        output_path = out_folder_from_files(input_files)
        count_files = len(input_files)
        converter.convert_files(input_files, output_path, args.input_format, args.output_format, count_files)


if __name__ == '__main__':
    log.logger.info('Start app.')
    main()
    log.logger.info('Finish app.')
