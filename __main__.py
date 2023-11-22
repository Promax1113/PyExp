from .cli import render_ui
from .file_management import sort_files
from .password_manager import get_pass
import choice
import os

while True:
    user = render_ui()
    if user == "Change Directory":
        dir_selection = choice.Input("Type in a full path: ", parser=str).ask()
        os.chdir(dir_selection)
    match user[1]:
        case "Sort Files":
            sort_files(os.getcwd(), choice.Menu(title="Choose a way of sorting:", choices=["date", "type"]).ask())
        
        case "Password Manager":
            get_pass()
        
        case "Exit":
            exit(0)
        case _:
            "Invalid!"