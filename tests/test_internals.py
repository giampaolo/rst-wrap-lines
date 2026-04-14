"""Tests for rst_wrap_lines.wrap_rst()."""

from . import InternalBaseTest


class TestProseParagraphs(InternalBaseTest):
    def test_long_paragraph_is_wrapped(self):
        src = (
            "This is a very long prose paragraph that clearly exceeds"
            " the default line length of seventy-nine characters and"
            " must therefore be wrapped.\n"
        )
        out = self.wrap(src)
        for line in out.splitlines():
            assert len(line) <= self.WIDTH
        self.assert_idempotent(src)

    def test_short_paragraph_unchanged(self):
        src = "Short paragraph.\n"
        assert self.wrap(src) == src
        self.assert_idempotent(src)

    def test_redundant_spaces_collapsed(self):
        src = "hello  world  foo.\n"
        out = self.wrap(src)
        assert "  " not in out
        self.assert_idempotent(src)

    def test_trailing_newline_preserved(self):
        src = "Some prose.\n"
        assert self.wrap(src).endswith("\n")
        self.assert_idempotent(src)

    def test_no_trailing_newline_preserved(self):
        src = "Some prose."
        assert not self.wrap(src).endswith("\n")
        self.assert_idempotent(src)


class TestPassthrough(InternalBaseTest):
    def test_section_title_unchanged(self):
        src = "My Section\n==========\n"
        assert self.wrap(src) == src
        self.assert_idempotent(src)

    def test_literal_block_unchanged(self):
        src = "Example::\n\n    some code here    with spaces\n"
        assert self.wrap(src) == src
        self.assert_idempotent(src)

    def test_grid_table_unchanged(self):
        src = "+-------+-------+\n| a     | b     |\n+-------+-------+\n"
        assert self.wrap(src) == src
        self.assert_idempotent(src)

    def test_comment_unchanged(self):
        src = ".. this is a comment\n   that spans two lines\n"
        assert self.wrap(src) == src
        self.assert_idempotent(src)

    def test_field_list_unchanged(self):
        src = ":Author: Giampaolo\n:Version: 1.0\n"
        assert self.wrap(src) == src
        self.assert_idempotent(src)


class TestInlineMarkup(InternalBaseTest):
    def test_inline_literal_not_broken(self):
        # ``like this`` must survive as an atomic token.
        src = "Prose with ``an inline literal that has spaces inside`` here.\n"
        out = self.wrap(src)
        assert "``an inline literal that has spaces inside``" in out
        self.assert_idempotent(src)

    def test_emphasis_not_broken(self):
        src = "Prose with *emphasized words across tokens* here.\n"
        out = self.wrap(src)
        assert "*emphasized words across tokens*" in out
        self.assert_idempotent(src)

    def test_role_not_broken(self):
        src = "See :func:`some function name` for details.\n"
        out = self.wrap(src)
        assert ":func:`some function name`" in out
        self.assert_idempotent(src)


class TestListItems(InternalBaseTest):
    def test_long_bullet_item_wrapped(self):
        src = (
            "- This bullet item is quite long and should be wrapped"
            " by the tool because it exceeds the maximum line length.\n"
        )
        out = self.wrap(src)
        for line in out.splitlines():
            assert len(line) <= self.WIDTH
        self.assert_idempotent(src)

    def test_short_bullet_item_unchanged(self):
        src = "- Short item.\n"
        assert self.wrap(src) == src
        self.assert_idempotent(src)

    def test_enumerated_list_wrapped(self):
        src = (
            "1. This enumerated item is quite long and should be"
            " wrapped by the tool because it exceeds the max width.\n"
        )
        out = self.wrap(src)
        for line in out.splitlines():
            assert len(line) <= self.WIDTH
        self.assert_idempotent(src)
