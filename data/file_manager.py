from dataclasses import dataclass
from json import load


@dataclass()
class DataModule:
    window_size: tuple = (400, 400)
    scale: tuple = (1, 1)
    simulation_time: int = 1000

    def __init__(self):
        with open("data/objects.json", "r") as read_file:
            self.objects = load(read_file)
        with open("data/UI/types_data.json", "r") as read_file:
            self.ui_objects = load(read_file)
        with open("settings.json", "r") as read_file:
            self.settings = load(read_file)
