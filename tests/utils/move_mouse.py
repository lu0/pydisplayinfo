import mouse


def move_mouse(x: int, y: int) -> None:
    """Sets coordinates of the mouse"""
    mouse.move(x, y, absolute=True, duration=0)


def get_mouse() -> None:
    """Get coordinates (x, y) of the mouse"""
    return mouse.get_position()
