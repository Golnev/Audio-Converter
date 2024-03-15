import logging
from logging.handlers import WatchedFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

file_handler = WatchedFileHandler('logger/my_conv.log', mode='w')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def directory_already_exist_log(dir_name: str, message: str):
    logger.error(f'"{dir_name}" - {message}')


def empty_folder_log(dir_name: str, message: str):
    logger.error(f'"{dir_name}" - {message}')


def wrong_format_main(message: str):
    logger.error(f'{message}. Non-existing format.')


def wrong_format_type_log(expected_format: str, received_format: str, message: str, other_description=''):
    logger.error(
        f'{message}. Expected format - "{expected_format}", received format - "{received_format}". {other_description}'
    )


def equal_format_type_log(message: str):
    logger.error(f'{message}')
