from utils.change_wallpaper import change_wallpaper
from utils.handle_db import read_data
from utils.menu_manager import menu_navigation


def main():
    change_wallpaper()


if __name__ == '__main__':
    container = read_data()
    menu_navigation(container)