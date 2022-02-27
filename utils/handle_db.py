import json
import os.path as path
from containers.container import Container


def write_data(in_data) -> None:
    out_data = []

    for item in in_data:
        out_data.append(item.__dict__)

    json_object = json.dumps(out_data)
    f = open("db/data.json", "w")
    f.write(json_object)


def read_data() -> Container:
    container = Container()
    if not path.isfile("db/data.json"):
        return container

    f = open("db/data.json")
    data = json.load(f)

    for item in data:
        container.store(item["name"])

    return container
