import os, pathlib, shutil

def create_file(dir):
    pass

def delete(dir: pathlib.Path, filename: str = None):
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