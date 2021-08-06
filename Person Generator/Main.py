from colorama import init
from controller.GeneratorController import GeneratorController

class Main:

    def __init__(self):
        init(autoreset = True)
        GeneratorController()

Main()