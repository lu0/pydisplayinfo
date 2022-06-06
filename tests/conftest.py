import pytest
from tests.utils import MockScreen, move_mouse

from pydisplayinfo import DisplayInfo


@pytest.fixture()
def display_info() -> DisplayInfo:
    """DisplayInfo with fixed size

    Since we do not know the actual resolution and position of the current
    display, we cannot compare the real output of the library with unknown
    values. However, we can fix the geometry and position of the root window
    (we'll need to move the mouse to this known position), and assume it
    represents a 'mock full screen window' expanded across the display.

    Cross-platform tests need to be executed manually on real environments, but
    future iterations may run these tests in an isolated environment through a
    CI/CD pipeline. Such environment will require a functional Window Manager.
    """
    # Move the mouse to a known position,
    # this will represent the "mock position" of the "current display"
    move_mouse(MockScreen.mouse_x, MockScreen.mouse_y)

    info = DisplayInfo()

    # TODO: Override the geometry of the window while testing (after creating
    # the functionality...), do not let it go full screen.
    info._test = True
    info._initial_dimensions = (MockScreen.width, MockScreen.height)

    yield info
    # info._window.destroy()
