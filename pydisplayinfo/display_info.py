from typing import Dict, Tuple

from pydisplayinfo import _HelperWindow

DEFAULT_SIZE = (200, 200)
DEFAULT_POSITION = (100, 100)


class DisplayInfo:
    def __init__(self, size=DEFAULT_SIZE, pos=DEFAULT_POSITION) -> None:
        """Get information of the current display

        Args:
            size (Tuple[int, int]): Initial width and height of the helper window
            pos (Tuple[int, int]): Initial x and y coordinates of the helper window
        """
        self.__window = _HelperWindow(*size, *pos)

    @property
    def _window(self) -> _HelperWindow:
        return self.__window

    @property
    def resolution(self) -> Tuple[int, int]:
        """Resolution of the current display"""
        self._window.expand_in_current()
        width = self._window.winfo_width()
        height = self._window.winfo_height()
        return (width, height)

    @property
    def offset_x(self) -> int:
        """X coordinate of the top-left corner of the current display"""
        self._window.expand_in_current()
        return self._window.winfo_x()

    @property
    def offset_y(self) -> int:
        """Y coordinate of the top-left corner of the current display"""
        self._window.expand_in_current()
        return self._window.winfo_y()

    @property
    def width(self) -> int:
        """Width (resolution along the X axis) of the current display"""
        self._window.expand_in_current()
        return self._window.winfo_width()

    @property
    def height(self) -> int:
        """Height (resolution along the X axis) of the current display"""
        self._window.expand_in_current()
        return self._window.winfo_height()

    @classmethod
    def all(cls) -> Dict:
        """All properties of the current display"""
        raise NotImplementedError
