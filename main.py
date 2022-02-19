import os
from dotenv import load_dotenv
import ctypes


class Main (object):
    def __init__(self):
        load_dotenv()
        
        file_name = input("Enter the file name: ")
        gallery_path = os.getenv("WALLPAPER_PATH")
        file_formater = os.getenv("IMAGE_FORMATER")

        path = f"{gallery_path}{file_name}.{file_formater}"
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 1)


Main()
