from utils.handle_db import read_data
from utils.menu_manager import menu_navigation


if __name__ == '__main__':
    container = read_data()
    menu_navigation(container)
