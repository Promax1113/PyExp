from fernet import Fernet
import hashlib, base64, json, os, pathlib

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
    f = Fernet(gen_fernet_key(key))
    to_enc = {}
    # Need to make it better
    to_enc["email"], to_enc["filename"] = input("E-Mail used for the password: "), input("Name for the file where the password is saved: ")
    with open(f"{dirname}/passwords/{to_enc['filename']}.passfile", "+wb") as file:
        file.write(f.encrypt(json.dumps(to_enc).encode()))
    print("Saved successfully!")
    
def read_password(key, name):
    f = Fernet(gen_fernet_key(key))
    with open(f"{dirname}/passwords/{name}", "rb") as file:
        return json.loads(f.decrypt(file.readline()))