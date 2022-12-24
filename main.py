from data.file_manager import DataModule
from data.engine import Engine
from data.interface import InterfaceHandler


settings_data = DataModule()
engine = Engine(settings_data)
UI = InterfaceHandler(settings_data, engine)


while settings_data.running:
    engine.interactions()
    UI.update()
