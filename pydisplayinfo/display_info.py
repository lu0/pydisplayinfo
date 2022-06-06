from tkinter import Tk
from typing import Tuple


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

    @property
    def all(self) -> Tuple:
        raise NotImplementedError
