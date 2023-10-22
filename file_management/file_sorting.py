import os, pathlib


def sort_files(dir, mode):
    if mode == "type":
        sort_type(dir)
    elif mode == "date":
        sort_date(dir)

def sort_date(dir):
    pass

def sort_type(dir):
    c_dir = os.getcwd()
    f_d = os.listdir(dir)
    files = []
    file_types = []
    for file in f_d:
        if os.path.isfile(f"{dir}/{file}"):
            files.append(file)

    for file in files:
        if os.path.isfile(file):
            file_types.append(pathlib.Path(file).suffix)
        else:
            continue
    os.chdir(dir)
    for file_type in file_types:
        pathlib.Path.mkdir(file_type, exist_ok=True)
    
    for file in files:
        os.rename(file, f"{dir}/{pathlib.Path(file).suffix}/{file}")

    os.chdir(c_dir)