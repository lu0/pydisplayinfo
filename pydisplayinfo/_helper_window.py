import tkinter
from tkinter import Tk
from typing import Tuple

DEFAULT_WIDTH = 150
DEFAULT_HEIGHT = 200
DEFAULT_X = 100
DEFAULT_Y = 120


class _HelperWindow(Tk):
    def __init__(
        self,
        width: int = DEFAULT_WIDTH,
        height: int = DEFAULT_HEIGHT,
        x: int = DEFAULT_X,
        y: int = DEFAULT_Y,
    ) -> None:
        """Create follower window

        Args:
            width (int): Initial width
            height (int): Initial height
            x (int): Initial x coordinate for the top-left corner
            y (int): Initial y coordinate for the top-left corner
        """

        self.__create_window()
        self.__remove_decorations()
        self.__initial_dimensions = (width, height)
        self.__initial_position = (x, y)
        self._reset_geometry()

    def __create_window(self):
        """Span a new helper window, remove old instances if any"""
        try:
            root: Tk = tkinter._default_root
            if root:
                root.destroy()
        except Exception:
            pass
        super().__init__()

    @property
    def windowing_system(self) -> str:
        # TODO: Make enum of windowing systems
        # TODO: Test on windows
        # TODO: Test on wayland
        return self.tk.call("tk", "windowingsystem")

    def __remove_decorations(self) -> None:
        if self.windowing_system == "x11":
            self.attributes("-type", "splash")
        else:
            self.overrideredirect(True)
        self.state("iconic")
        self.update_idletasks()

    @property
    def initial_dimensions(self) -> Tuple[int, int]:
        """Get initial width and height of the window"""
        return self.__initial_dimensions

    @property
    def initial_position(self) -> Tuple[int, int]:
        """Get initial x and y coordinates of the window"""
        return self.__initial_position

    def _reset_geometry(self) -> None:
        """Set geometry to the size and position defined during instantiation"""
        self.__set_geometry(*self.initial_dimensions, *self.initial_position)

    def __set_geometry(self, width: int, height: int, x: int, y: int) -> None:
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.update_idletasks()

    def expand_in_current(self) -> None:
        """Expand window across the current display"""
        self._reset_geometry()
        self._move_to_mouse_location()
        self._make_fullscreen()

    def _move_to_mouse_location(self) -> None:
        mouse_location: Tuple[int, int] = self.winfo_pointerxy()
        self.__move(*mouse_location)

    def __move(self, x: int, y: int) -> None:
        current_width: int = self.winfo_width()
        current_height: int = self.winfo_height()
        self.__set_geometry(current_width, current_height, x, y)

    def _make_fullscreen(self) -> None:
        if self.windowing_system == "x11":
            self.attributes("-type", "normal")
            self.attributes("-fullscreen", True)
        else:
            self.attributes("-zoomed", True)
        self.update()

    def __resize(self, width: int, height: int) -> None:
        current_x: int = self.winfo_x
        current_y: int = self.winfo_y
        self.__set_geometry(width, height, current_x, current_y)
