import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Audio Converter')
    parser.add_argument('--input_format', help='Enter what format to convert from.')
    parser.add_argument('--output_format', help='Enter what format to convert to.')

    parser.add_argument('--from_directory',
                        nargs='?',
                        const='window',
                        help='Enter the directory to convert from or leave blank for input via the dialogue box',
                        )
    parser.add_argument('--path_files',
                        nargs='?',
                        const='window',
                        help='Enter path of file or files to convert from '
                             'or leave blank for input via the dialogue box',
                        )
    args = parser.parse_args()

    if not (args.from_directory or args.path_files):
        args.path_files = 'window'

    elif args.from_directory and args.path_files:
        parser.error('Only one of --from_directory or --path_files can be provided')

    return args
