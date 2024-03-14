from pydub import AudioSegment
import os

from exceptions.exceptions import DirectoryAlreadyExistException, FormatException
import logger.logging_config as log
from config.work_folders import input_path, output_path, file_len, make_dir


def main():
    count = 0
    with_errors = 0
    executed = 0

    try:
        make_dir(input_path, output_path)
    except DirectoryAlreadyExistException as e:
        log.directory_already_exist_log(os.path.basename(output_path), e.message)
        return

    for obj in os.scandir(input_path):
        try:
            if obj.path.endswith('.flac'):
                out = output_path + '\\' + os.path.splitext(os.path.basename(obj.path))[0] + '.mp3'
                AudioSegment.from_file(obj.path, format='flac').export(out, format='mp3')
                count += 1
                executed += 1
                log.logger.info(f'{count} of {file_len} - {os.path.splitext(os.path.basename(obj.path))[0]}')
            else:
                count += 1
                with_errors += 1
                raise FormatException
        except FormatException as e:
            log.wrong_format_type_log('flac', os.path.splitext(os.path.basename(obj.path))[1], e.message,
                                      f'{count} of {file_len}. '
                                      f'{os.path.splitext(os.path.basename(obj.path))[0]}'
                                      )

    log.logger.info(
        f'Conversion from the "{input_path}" folder is done. '
        f'Executed: {executed}, Unfulfilled (with errors): {with_errors}'
    )


if __name__ == '__main__':
    log.logger.info('Start app.')
    main()
    log.logger.info('Finish app.')
