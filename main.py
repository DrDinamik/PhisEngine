import pygame.examples.eventlist
from data.file_manager import DataModule
from data.engine import Engine
from data.interface import InterfaceHandler
from data.utilities import Connector


# pygame.examples.eventlist.main()


settings_data = DataModule()
engine = Engine(settings_data)
UI = InterfaceHandler(settings_data, engine)
connector = Connector(settings_data, UI, engine)  # Yet doing nothing

while True:
    UI.update()
    engine.interactions(lambda x, y: abs(x) ** -1 * x * y)
