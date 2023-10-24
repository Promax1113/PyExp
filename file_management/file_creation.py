import os, pathlib, shutil

def create(dir, filename = None):
    try:
        if filename:
            file = open(f"{dir}/{filename}", "x")
            file.close()
        elif not filename:
            pathlib.Path.mkdir(dir)
    except FileExistsError:
        print("File already exists.")

def delete(dir, filename = None):
    try:
        if filename:
            os.remove(f"{dir}/{filename}")
        elif not filename:
            if input("This will forcefully remove all files inside the dir and the dir itself! Are you sure? (y/N): ").upper() == "Y":
                shutil.rmtree(dir)
                print("Removed!")
            else:
                print("No file was removed!")
    
    except FileNotFoundError:
        print("File was not found!")

def move(dir, new_dir, filename = None):
    try:
        if not filename:
            shutil.move(dir, new_dir)
        else:
            os.rename(f"{dir}/{filename}", f"{new_dir}/{filename}")
    except (FileNotFoundError, FileExistsError):
        print("Either file does not exist or there's a file with the same name already in destination!")