import os
from datetime import datetime
import choice, json

def render_ui():
    directory = os.listdir(os.getcwd())
    file_data = [{'filename': filename, 'stats': {"size": os.stat(filename).st_size, 'st_atime': datetime.fromtimestamp(os.stat(filename).st_atime).strftime("%d-%m-%Y %H:%M"), 'st_mtime': datetime.fromtimestamp(os.stat(filename).st_mtime).strftime("%d-%m-%Y %H:%M"), 'st_ctime': datetime.fromtimestamp(os.stat(filename).st_ctime).strftime("%d-%m-%Y %H:%M")}, 'isdir': os.path.isdir(filename)} for filename in directory]
    file_data_str = [f"{filename['filename']} - {filename['stats']['size']} Bytes - Last modified: {filename['stats']["st_mtime"]}" for filename in file_data]
    file_data_str.append("Change Directory")
    user = choice.Menu(file_data_str, global_actions=["Sort Files", "Password Manager", "Exit"],title="Choose a directory / file to perform an action on:").ask()
    return user