import os
import sys
from typing import Literal, Tuple

from pydub import AudioSegment

import src.logger.logging_config as log
from src.work_dirs.work_folders import remove_dir
from src.exceptions.exceptions import EqualFormatTypesException, WrongFormatException, EmptyDirectoryException

type_formats_lit = Literal['wav', 'mp3', 'aiff', 'flac', 'ogg', 'aac', 'm4a', 'wma', 'au', 'opus']


class Converter:
    type_formats = ['wav', 'mp3', 'aiff', 'flac', 'ogg', 'aac', 'm4a', 'wma', 'au', 'opus']

    def __init__(self):
        self.count = 0
        self.with_errors = 0
        self.executed = 0

    def _check_format(self, format_from: type_formats_lit, format_to: type_formats_lit, output_path: str = None):
        try:
            if format_from not in self.type_formats or format_to not in self.type_formats:
                raise WrongFormatException
        except WrongFormatException as e:
            remove_dir(output_path)
            log.wrong_format_main(e.message)
            sys.exit(1)

    @staticmethod
    def _check_directory_len(file_len: int, input_path: str, output_path: str):
        try:
            if file_len == 0:
                raise EmptyDirectoryException
        except EmptyDirectoryException as e:
            remove_dir(output_path)
            log.empty_folder_log(input_path, e.message)
            sys.exit(1)

    @staticmethod
    def _check_equal_format(format_from: type_formats_lit, format_to: type_formats_lit, output_path: str = None):
        try:
            if format_from == format_to:
                raise EqualFormatTypesException
        except EqualFormatTypesException as e:
            remove_dir(output_path)
            log.equal_format_type_log(e.message)
            sys.exit(1)

    def convert_from_dir(self, input_path: str,
                         output_path: str,
                         format_from: type_formats_lit,
                         format_to: type_formats_lit,
                         file_len: int):

        self._check_format(format_from, format_to, output_path)
        self._check_directory_len(file_len, input_path, output_path)
        self._check_equal_format(format_from, format_to, output_path)

        for obj in os.scandir(input_path):
            try:
                if obj.path.endswith('.' + format_from):
                    out = output_path + '\\' + os.path.splitext(os.path.basename(obj.path))[0] + '.' + format_to
                    AudioSegment.from_file(obj.path, format=format_from).export(out, format=format_to)
                    self.count += 1
                    self.executed += 1
                    log.logger.info(f'{self.count} of {file_len} - {os.path.splitext(os.path.basename(obj.path))[0]}')
                else:
                    self.count += 1
                    self.with_errors += 1
                    raise WrongFormatException
            except WrongFormatException as e:
                log.wrong_format_type_log(format_from, os.path.splitext(os.path.basename(obj.path))[1][1:], e.message,
                                          f'{self.count} of {file_len}. '
                                          f'{os.path.splitext(os.path.basename(obj.path))[0]}'
                                          )

        self._end(input_path, output_path)

    def convert_files(self, input_files: Tuple[str, ...],
                      output_path: str,
                      format_from: type_formats_lit,
                      format_to: type_formats_lit,
                      count_files: int
                      ):
        self._check_format(format_from, format_to)
        self._check_equal_format(format_from, format_to, output_path)
        for file in input_files:
            pass

    def _end(self, input_path: str, output_path: str):
        if self.count == self.with_errors:
            log.logger.info('All elements were converted with errors.')
            remove_dir(output_path)

        log.logger.info(
            f'Conversion from the "{input_path}" folder is done. '
            f'Executed: {self.executed}, Unfulfilled (with errors): {self.with_errors}'
        )
