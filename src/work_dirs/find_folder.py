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


def len_folder(in_path: str) -> int:
    return len([file for file in os.scandir(in_path) if file.is_file()])


if __name__ == '__main__':
    print(find_files())
