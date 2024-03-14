import os

from pydub import AudioSegment

import logger.logging_config as log
from exceptions.exceptions import FormatException


def converter(input_path: str, output_path: str, format_from: str, format_to: str, file_len: int):
    count = 0
    with_errors = 0
    executed = 0

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
                raise FormatException
        except FormatException as e:
            log.wrong_format_type_log(format_from, os.path.splitext(os.path.basename(obj.path))[1], e.message,
                                      f'{count} of {file_len}. '
                                      f'{os.path.splitext(os.path.basename(obj.path))[0]}'
                                      )

    log.logger.info(
        f'Conversion from the "{input_path}" folder is done. '
        f'Executed: {executed}, Unfulfilled (with errors): {with_errors}'
    )
