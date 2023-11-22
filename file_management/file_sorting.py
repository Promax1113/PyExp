import os
import pathlib
from datetime import datetime


def sort_files(directory, mode):
    if mode == "type":
        sort_type(directory)
    elif mode == "date":
        sort_date(directory)
    else:
        raise NameError("Mode was not found!")


def sort_date(directory):
    c_dir = os.getcwd()
    f_d = os.listdir(directory)
    files = []
    file_dates = []
    for file in f_d:
        if os.path.isfile(f"{directory}/{file}"):
            files.append(file)

    for file in files:
        file_dates.append(pathlib.Path(datetime.fromtimestamp(os.path.getctime(f"{directory}/{file}")).strftime("%d-%m-%Y")))

    os.chdir(directory)
    for date in file_dates:
        pathlib.Path.mkdir(date, exist_ok=True)

    for file in files:
        os.rename(file,
                  f"{directory}/{pathlib.Path(datetime.fromtimestamp(os.path.getctime(f'{directory}/{file}')).strftime('%d-%m-%Y'))}/{file}")
    os.chdir(c_dir)


def sort_type(directory):
    c_dir = os.getcwd()
    f_d = os.listdir(directory)
    files = []
    file_types = []
    for file in f_d:
        if os.path.isfile(f"{directory}/{file}"):
            files.append(file)

    for file in files:
        file_types.append(pathlib.Path(pathlib.Path(file).suffix))

    os.chdir(directory)
    for file_type in file_types:
        pathlib.Path.mkdir(file_type, exist_ok=True)

    for file in files:
        os.rename(file, f"{directory}/{pathlib.Path(file).suffix}/{file}")

    os.chdir(c_dir)
