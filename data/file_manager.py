from dataclasses import dataclass
from json import load
import sys
from os.path import abspath, join


@dataclass()
class DataModule:
    size: tuple
    scale: tuple
    dyn_scale: float
    running: bool = True
    simulation_time: int = 60

    def __init__(self):
        with open(get_resources("data/objects.json")) as read_file:
            self.objects = load(read_file)
        with open(get_resources("data/UI/types_data.json")) as read_file:
            self.ui_objects = load(read_file)
        with open(get_resources("settings.json")) as read_file:
            self.settings = load(read_file)
        self.size = tuple(self.settings["size"])
        self.scale = tuple(self.settings["scale"])
        self.dyn_scale = self.settings["dyn_scale"]

    def logger(self, name, data):
        with open(get_resources(f"logs\log_{name}.txt"), "a") as file:
            file.write(data)


def get_resources(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = abspath(".")

    return join(base_path, relative_path)
