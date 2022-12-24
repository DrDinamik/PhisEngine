from dataclasses import dataclass
from json import load


@dataclass()
class DataModule:
    size: tuple
    scale: tuple
    running: bool = True
    simulation_time: int = 60
    dyn_scale: float = 2.0e+9 ** -1

    def __init__(self):
        with open("data/objects.json", "r") as read_file:
            self.objects = load(read_file)
        with open("data/UI/types_data.json", "r") as read_file:
            self.ui_objects = load(read_file)
        with open("settings.json", "r") as read_file:
            self.settings = load(read_file)
        self.size = tuple(self.settings["size"])
        self.scale = tuple(self.settings["scale"])
