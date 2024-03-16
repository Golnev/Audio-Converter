import os

from pydub import AudioSegment

import src.logger.logging_config as log
from src.work_dirs.work_folders import remove_dir
from src.exceptions.exceptions import EqualFormatTypesException, WrongFormatException, EmptyDirectoryException

type_formats = ['wav', 'mp3', 'aiff', 'flac', 'ogg', 'aac', 'm4a', 'wma', 'au', 'opus']


def converter(input_path: str,
              output_path: str,
              format_from: str,
              format_to: str,
              file_len: int) -> None:
    count = 0
    with_errors = 0
    executed = 0

    try:
        if format_from not in type_formats or format_to not in type_formats:
            raise WrongFormatException
    except WrongFormatException as e:
        log.wrong_format_main(e.message)

    try:
        if not file_len:
            raise EmptyDirectoryException
    except EmptyDirectoryException as e:
        remove_dir(output_path)
        log.empty_folder_log(input_path, e.message)
        return

    try:
        if format_from == format_to:
            raise EqualFormatTypesException
    except EqualFormatTypesException as e:
        remove_dir(output_path)
        log.equal_format_type_log(e.message)
        return

    for obj in os.scandir(input_path):
        try:
            if obj.path.endswith('.' + format_from):
                out = output_path + '\\' + os.path.splitext(os.path.basename(obj.path))[0] + '.' + format_to
                AudioSegment.from_file(obj.path, format=format_from).export(out, format=format_to)
                count += 1
                executed += 1
                log.logger.info(f'{count} of {file_len} - {os.path.splitext(os.path.basename(obj.path))[0]}')
            else:
                count += 1
                with_errors += 1
                raise WrongFormatException
        except WrongFormatException as e:
            log.wrong_format_type_log(format_from, os.path.splitext(os.path.basename(obj.path))[1][1:], e.message,
                                      f'{count} of {file_len}. '
                                      f'{os.path.splitext(os.path.basename(obj.path))[0]}'
                                      )

    if count == with_errors:
        log.logger.info('All elements were converted with errors.')
        remove_dir(output_path)

    log.logger.info(
        f'Conversion from the "{input_path}" folder is done. '
        f'Executed: {executed}, Unfulfilled (with errors): {with_errors}'
    )
