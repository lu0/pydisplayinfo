import mouse


def move_mouse(x: int, y: int) -> None:
    mouse.move(x, y, absolute=True, duration=0)
