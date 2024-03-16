import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Audio Converter')
    parser.add_argument('--input_format', help='Enter what format to convert from.')
    parser.add_argument('--output_format', help='Enter what format to convert to.')
    parser.add_argument('--from_directory', help='Enter the directory to convert from.')
    return parser.parse_args()
