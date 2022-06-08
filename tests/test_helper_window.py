import logging
import tkinter

import pytest
from tests.utils import get_mouse, move_mouse

from pydisplayinfo import _HelperWindow

log = logging.getLogger()
log.setLevel(level=logging.INFO)

INITIAL_WIDTH = 170
INITIAL_HEIGHT = 200
INITIAL_X = 90
INITIAL_Y = 100


@pytest.fixture()
def helper_window() -> _HelperWindow:
    prev_mouse_x, prev_mouse_y = get_mouse()
    yield _HelperWindow(
        width=INITIAL_WIDTH,
        height=INITIAL_HEIGHT,
        x=INITIAL_X,
        y=INITIAL_Y,
    )
    move_mouse(prev_mouse_x, prev_mouse_y)
    try:
        stale_window: _HelperWindow = tkinter._default_root
        if stale_window:
            stale_window.destroy()
    except Exception:
        pass


class TestHelperWindow:
    def test_property_initial_dimensions(self, helper_window: _HelperWindow):
        assert helper_window.initial_dimensions == (INITIAL_WIDTH, INITIAL_HEIGHT)

    def test_property_initial_position(self, helper_window: _HelperWindow):
        assert helper_window.initial_position == (INITIAL_X, INITIAL_Y)

    def test_reset_geometry(self, helper_window: _HelperWindow):
        assert helper_window.geometry() == "{}x{}+{}+{}".format(
            INITIAL_WIDTH, INITIAL_HEIGHT, INITIAL_X, INITIAL_Y
        )

    def test_move_to_mouse_location(self, helper_window: _HelperWindow):
        move_mouse(INITIAL_X, INITIAL_Y)
        helper_window._move_to_mouse_location()
        assert helper_window.winfo_x() == INITIAL_X
        assert helper_window.winfo_y() == INITIAL_Y

    def test_expand_in_current_display(self, helper_window: _HelperWindow):
        helper_window.expand_in_current()
        # TODO: Check if geometry match with current display (manually :/)
        log.debug(f"Fullscreen geometry: {helper_window.geometry()}")
