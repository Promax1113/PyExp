import os
import hashlib
from getpass import getpass
from.password_access import save_password

pass_dir = "pass.hash"

def get_pass():

    status = lambda x: "Success!" if x == 200 else "Unauthorised!"

    password = getpass().encode()
    result = status(check_login(hashlib.sha256(password).hexdigest()))
    print(result)

    while result == "Unauthorised!":
        password = getpass().encode()
        result = status(check_login(hashlib.sha256(password).hexdigest()))
        print(result)
    save_password(password)

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