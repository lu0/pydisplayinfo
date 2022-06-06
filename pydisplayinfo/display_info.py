from tkinter import Tk
from typing import Dict, Tuple


class DisplayInfo:
    def __init__(self) -> None:
        pass

    @property
    def _window(self) -> Tk:
        raise NotImplementedError

    @property
    def resolution(self) -> Tuple[int, int]:
        """Resolution of the current display"""
        raise NotImplementedError

    @property
    def offset_x(self) -> int:
        """X coordinate of the top-left corner of the current display"""
        raise NotImplementedError

    @property
    def offset_y(self) -> int:
        """Y coordinate of the top-left corner of the current display"""
        raise NotImplementedError

    @property
    def width(self) -> int:
        """Width (resolution along the X axis) of the current display"""
        raise NotImplementedError

    @property
    def height(self) -> int:
        """Height (resolution along the X axis) of the current display"""

        raise NotImplementedError

    @classmethod
    def all(cls) -> Dict:
        """All properties of the current display"""
        raise NotImplementedError
