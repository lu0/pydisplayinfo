import logging
from argparse import ArgumentParser as Parser

import pytest
from tests.utils import MockScreen

from pydisplayinfo import __main__ as command_display_info

log = logging.getLogger()
log.setLevel(level=logging.INFO)


CLI_COMPLETE_OUTPUT = f"""
{MockScreen.width}x{MockScreen.height}
{MockScreen.mouse_x}
{MockScreen.mouse_y}
{MockScreen.width}
{MockScreen.height}
"""


class TestDisplayCLI:
    @pytest.mark.parametrize(
        "arg, expected_output",
        [
            ("--show", CLI_COMPLETE_OUTPUT),
            ("--res", f"{MockScreen.width}x{MockScreen.height}"),
            ("--offset-x", MockScreen.mouse_x),
            ("--offset-y", MockScreen.mouse_y),
            ("--width", MockScreen.width),
            ("--height", MockScreen.height),
        ],
    )
    def test_cli_output(self, cli_parser: Parser, arg: str, expected_output: str):
        cli_args = cli_parser.parse_args([arg])
        output = command_display_info.main(cli_args)
        assert output == expected_output
