import os, pathlib
from datetime import datetime


def sort_files(dir, mode):
    if mode == "type":
        sort_type(dir)
    elif mode == "date":
        sort_date(dir)
    else:
        raise NameError("Mode was not found!")

def sort_date(dir):
    c_dir = os.getcwd()
    f_d = os.listdir(dir)
    files = []
    file_dates = []
    for file in f_d:
        if os.path.isfile(f"{dir}/{file}"):
            files.append(file)

    for file in files:
        file_dates.append(pathlib.Path(datetime.fromtimestamp(os.path.getctime(f"{dir}/{file}")).strftime("%d-%m-%Y")))

    os.chdir(dir)
    for date in file_dates:
        pathlib.Path.mkdir(date, exist_ok=True)

    for file in files:
        os.rename(file, f"{dir}/{pathlib.Path(datetime.fromtimestamp(os.path.getctime(f'{dir}/{file}')).strftime('%d-%m-%Y'))}/{file}")
    os.chdir(c_dir)

def sort_type(dir):
    c_dir = os.getcwd()
    f_d = os.listdir(dir)
    files = []
    file_types = []
    for file in f_d:
        if os.path.isfile(f"{dir}/{file}"):
            files.append(file)

    for file in files:
        file_types.append(pathlib.Path(pathlib.Path(file).suffix))

    os.chdir(dir)
    for file_type in file_types:
        pathlib.Path.mkdir(file_type, exist_ok=True)
    
    for file in files:
        os.rename(file, f"{dir}/{pathlib.Path(file).suffix}/{file}")

    os.chdir(c_dir)