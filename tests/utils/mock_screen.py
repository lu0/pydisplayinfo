from dataclasses import dataclass


@dataclass
class MockScreen:
    width: int = 500
    height: int = 600
    mouse_x: int = 200
    mouse_y: int = 100
