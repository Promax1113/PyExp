import base64
import hashlib
import json
import os
from getpass import getpass
import fernet

pass_path_R = lambda x: x.split("\\") if os.name == 'nt' else x.split("/")
pass_path = list(pass_path_R(os.path.realpath(__file__)))
pass_path.pop(-1)
dirname = '/'.join(pass_path)


def gen_fernet_key(passcode: bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))


def save_password(key):
    f = fernet.Fernet(gen_fernet_key(key))
    to_enc = {"email": input("E-Mail used for the password: "), "filename": input(
        "Name for the file where the password is saved: "), "password": getpass("Enter the password used: ")}
    # Need to make it better
    with open(f"{dirname}/passwords/{to_enc['filename']}.passfile", "+wb") as file:
        file.write(f.encrypt(json.dumps(to_enc).encode()))
    print("Saved successfully!")


def read_password(key, name):
    f = fernet.Fernet(gen_fernet_key(key))
    try:
        with open(f"{dirname}/passwords/{name}", "rb") as file:
            return json.loads(f.decrypt(file.readline()))
    except fernet.InvalidToken:
        print("Invalid password used to decrypt. Did you delete the pass.hash or used another password to log in?")
        return "401, Unauthorised"
