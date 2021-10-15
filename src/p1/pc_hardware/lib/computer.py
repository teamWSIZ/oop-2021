from lib.components.motherboard import Motherboard

class Computer:
    __motherboard: Motherboard
    __is_running: bool

    def __init__(self):
        self.__motherboard = None
        self.__is_running = False

    def __repr__(self):
        components = '\n'.join([f' > {x}' for x in [
            self.__motherboard.cpu,
            self.__motherboard.ram,
            self.__motherboard.disks
        ]]) 
        return f'Running: {self.__is_running}\nComponents:\n{components}'

    def set_motherboard(self, motherboard):
        if not type(motherboard) == Motherboard:
            raise RuntimeError("It's not a motherboard")
        self.__motherboard = motherboard
        self.__motherboard.computer = self

    @property
    def motherboard(self) -> Motherboard:
        return self.__motherboard

    def run(self):
        if self.__is_running:
            raise RuntimeError("Computer is already running")

        self.__is_running = True

    def stop(self):
        if not self.__is_running:
            raise RuntimeError("Computer is not running")

        self.__is_running = False

    @property
    def is_running(self):
        return self.__is_running
