import tkinter as tk
from tkinter import filedialog


def find_folder():
    root = tk.Tk()
    root.withdraw()

    selected_folder = filedialog.askdirectory()

    return selected_folder
