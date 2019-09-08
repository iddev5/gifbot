import importlib

def import_command(name: str):
    i = importlib.import_module('command.'+name)
    return i
