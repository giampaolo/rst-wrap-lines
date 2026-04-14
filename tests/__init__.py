"""Test utils."""

import pathlib

from rst_wrap_lines import wrap_rst

TESTS_DIR = pathlib.Path(__file__).parent


class InternalBaseTest:
    WIDTH = 79

    def wrap(self, source, width=None):
        if width is None:
            width = self.WIDTH
        return wrap_rst(source, width)

    def assert_idempotent(self, source, width=None):
        """Assert that wrapping twice yields the same output as once."""
        if width is None:
            width = self.WIDTH
        first = wrap_rst(source, width)
        second = wrap_rst(first, width)
        assert first == second
