from InquirerPy import prompt
import os
from utils.handle_db import write_data
from utils.menu_options import add_wallpaper, delete_wallpaper, set_wallpaper


def make_menu():
    questions = [
        {
            "type": "list",
            "name": "opt",
            "message": "What would you like to do?",
            "choices": [
                {
                    "value": "1",
                    "name": "1. Set wallpaper"
                },
                {
                    "value": "2",
                    "name": "2. Add wallpaper"
                },
                {
                    "value": "3",
                    "name": "3. Remove wallpaper"
                },
                {
                    "value": "0",
                    "name": "4. Exit"
                }
            ]
        }
    ]

    result = prompt(questions)
    return result["opt"]


def menu_navigation(container):
    opt = ""
    while opt != "0":
        os.system("clear")
        opt = make_menu()

        if opt == "1":
            set_wallpaper(container)

        elif opt == "2":
            add_wallpaper(container)

        elif opt == "3":
            delete_wallpaper(container)

        if opt != "0":
            input("Press ENTER to continue")
    
    write_data(container.list)
