from InquirerPy import prompt

from utils.change_wallpaper import change_wallpaper


def list_wallpaper(container) -> str:
    choices = []
    acc = 1
    for wallpaper in container.list:
        choices.append(
            {"value": wallpaper.name, "name": f"{acc}. {wallpaper.name}"})
        acc += 1

    choices.append({"value": "0", "name": "\nCancel"})

    questions = [
        {
            "type": "list",
            "name": "opt",
            "message": "Select a wallpaper",
            "choices": choices
        }
    ]

    result = prompt(questions)

    return result["opt"]


def add_wallpaper(container) -> None:
    name = input("Enter the wallpaper file name with out the extension: ")
    if not name:
        print("Enter a valid wallpaper name")
        input("Press ENTER to continue: ")
        return

    container.store(name)
    pass


def set_wallpaper(container) -> None:

    opt = list_wallpaper(container)

    if opt == "0":
        return

    change_wallpaper(opt)


def delete_wallpaper(container) -> None:

    opt = list_wallpaper(container)

    if opt == "0":
        return

    container.destroy(opt)
