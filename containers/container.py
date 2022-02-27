from models.wallpaper import Wallpaper


class Container (object):

    def __init__(self) -> None:
        self.list = []

    def store(self, name) -> None:
        wallpaper = Wallpaper(name)
        self.list.append(wallpaper)

    def destroy(self, name) -> None:
        for i in range(len(self.list)):
            if self.list[i].name == name:
                self.list.pop(i)
                print("The wallpaper was deleted successfully")
                return
        print("The wallpaper does not exist")
