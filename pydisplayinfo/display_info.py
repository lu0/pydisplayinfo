from tkinter import Tk
from typing import Dict


class DisplayInfo:
    def __init__(self) -> None:
        pass

    @property
    def _window(self) -> Tk:
        raise NotImplementedError

    @property
    def width(self):
        raise NotImplementedError

    @property
    def height(self):
        raise NotImplementedError

    @property
    def offset_x(self):
        raise NotImplementedError

    @property
    def offset_y(self):
        raise NotImplementedError

    @property
    def resolution(self):
        raise NotImplementedError

    @classmethod
    def all(cls) -> Dict:
        raise NotImplementedError
