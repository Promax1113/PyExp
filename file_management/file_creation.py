import os
import pathlib
import shutil


def create(directory, filename=None):
    try:
        if filename:
            file = open(f"{directory}/{filename}", "x")
            file.close()
        elif not filename:
            pathlib.Path.mkdir(directory)
    except FileExistsError:
        print("File already exists.")


def delete(directory, filename=None):
    try:
        if filename:
            os.remove(f"{directory}/{filename}")
        elif not filename:
            if input(
                    "This will forcefully remove all files inside the dir and the dir itself! Are you sure? (y/N): ").upper() == "Y":
                shutil.rmtree(directory)
                print("Removed!")
            else:
                print("No file was removed!")

    except FileNotFoundError:
        print("File was not found!")


def move(directory, new_dir, filename=None):
    try:
        if not filename:
            shutil.move(directory, new_dir)
        else:
            os.rename(f"{directory}/{filename}", f"{new_dir}/{filename}")
    except (FileNotFoundError, FileExistsError):
        print("Either file does not exist or there's a file with the same name already in destination!")
