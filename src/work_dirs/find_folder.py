import os
import tkinter as tk
from tkinter import filedialog


def find_folder() -> str:
    root = tk.Tk()
    root.withdraw()

    selected_folder = filedialog.askdirectory()

    root.destroy()

    return selected_folder


def find_files() -> (str, ...):
    root = tk.Tk()
    root.withdraw()

    select_files = filedialog.askopenfilenames()

    root.destroy()

    return select_files


def out_folder(in_path: str) -> str:
    return f'{os.path.dirname(in_path)}\\{os.path.basename(in_path)}_CONV'


def out_folder_from_files(in_paths: (str, ...)) -> str:
    return f'{os.path.dirname(in_paths[0])}'


def len_folder(in_path: str) -> int:
    return len([file for file in os.scandir(in_path) if file.is_file()])


if __name__ == '__main__':
    input_file = find_files()
    res = (out_folder_from_files(input_file))
    print(res)

