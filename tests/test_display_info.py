import logging

from tests.utils import MockScreen

from pydisplayinfo import DisplayInfo

log = logging.getLogger()
log.setLevel(level=logging.INFO)


class TestDisplayInfo:
    def test_resolution(self, display_info: DisplayInfo):
        assert display_info.resolution == (MockScreen.width, MockScreen.height)

    def test_display_offset_x_is_mouse_x(self, display_info: DisplayInfo):
        assert display_info.offset_x == MockScreen.mouse_x

    def test_display_offset_y_is_mouse_y(self, display_info: DisplayInfo):
        assert display_info.offset_y == MockScreen.mouse_y

    def test_display_width(self, display_info: DisplayInfo):
        assert display_info.width == MockScreen.width

    def test_display_height(self, display_info: DisplayInfo):
        assert display_info.height == MockScreen.height

    def test_summarized_info(self, display_info: DisplayInfo):
        assert display_info.all() == dict(
            resolution=({MockScreen.width}, {MockScreen.height}),
            offset_x=MockScreen.mouse_x,
            offset_y=MockScreen.mouse_y,
            width=MockScreen.width,
            height=MockScreen.height,
        )
