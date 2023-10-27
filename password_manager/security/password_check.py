import os
import hashlib
from getpass import getpass
from .password_access import *
import choice

pass_dir = "pass.hash"

def get_pass():
    global pass_path
    if not "passwords" in os.listdir():
        pass_path_R = lambda x: x.split("\\") if os.name == 'nt' else x.split("/")
        pass_path = list(pass_path_R(os.path.realpath(__file__)))
        pass_path.pop(-1)
        pass_path = '/'.join(pass_path)
        
        pathlib.Path.mkdir(pathlib.Path(f"{pass_path}/passwords"), exist_ok=True)

    status = lambda x: "Success!" if x == 200 else "Unauthorised!"

    password = getpass().encode()
    result = status(check_login(hashlib.sha256(password).hexdigest()))
    print(result)

    while result == "Unauthorised!":
        password = getpass().encode()
        result = status(check_login(hashlib.sha256(password).hexdigest()))
        print(result)
    

    while True:
        try:
            user = choice.Menu(["Save a password", "Read a password", "Back to explorer"], title="Choose an option:").ask()

        except TypeError:
            print("Invalid choice!")
            user = None

        if user == "Save a password":
            save_password(password)
        elif user == "Read a password":
            try:
                passes = os.listdir(f"{pass_path}/passwords")
                if len(passes) == 0:
                    print("\nNo passwords found!\n")
                    continue
            except FileNotFoundError:
                print("Passwords directory was not found!")
                continue
            user = choice.Menu(passes).ask()
            print(read_password(password, user))
        elif user == "Back to explorer":
            break
        
def check_login(pass_hash):
    global pass_dir
    if not os.path.isfile("pass.hash"):
        return save_login(pass_hash)
    else:
        with open(pass_dir, "r") as f:
            if f.readline() == pass_hash: return 200
            else: return 401


def save_login(pass_hash):
    global pass_dir
    with open(pass_dir, "w") as f:
        f.write(pass_hash)
        return 200