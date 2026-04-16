"""Tests for RST constructs that must pass through verbatim."""

from . import BaseTest


class TestPassthrough(BaseTest):
    def test_section_title_unchanged(self):
        src = "My Section\n==========\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_section_with_overline_unchanged(self):
        src = "========\nOverline\n========\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_short_underline_not_treated_as_title(self):
        # An underline shorter than the preceding text is not a title
        # (docutils treats it as prose). The tool must not merge the
        # text line with the underline as if it were a title, and must
        # not merge the underline into following prose either.
        src = "Long line of text that is not a title\n---\nMore prose.\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_literal_block_unchanged(self):
        src = "Example::\n\n    some code here    with spaces\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_block_quote_unchanged(self):
        # An indented block not introduced by '::' is a block quote.
        src = "Paragraph.\n\n    Indented block quote.\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_grid_table_unchanged(self):
        src = "+-------+-------+\n| a     | b     |\n+-------+-------+\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_simple_table_unchanged(self):
        src = "===  ===\na    b\n===  ===\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_comment_unchanged(self):
        src = ".. this is a comment\n   that spans two lines\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_field_list_unchanged(self):
        src = ":Author: Giampaolo\n:Version: 1.0\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_field_list_with_spaces_in_name_unchanged(self):
        src = ":type exc_info: bool\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_definition_list_term_unchanged(self):
        # The term line must not be wrapped into the definition body.
        src = "term\n    Definition text.\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_hyperlink_target_unchanged(self):
        src = ".. _some target: https://example.com\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_transition_unchanged(self):
        src = "Paragraph.\n\n----------\n\nAnother paragraph.\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_field_list_long_value_unchanged(self):
        # A field list entry whose value exceeds WIDTH must not be
        # wrapped -- the tool should not treat it as prose.
        src = (
            ":Author: A very long author name that goes on"
            " and on and exceeds the target width of seventy-nine"
            " characters easily\n"
        )
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_option_list_unchanged(self):
        # Option list items must not be merged into a prose paragraph.
        src = "-f FILE  Input file.\n-o FILE  Output file.\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_option_list_long_option_unchanged(self):
        src = (
            "--output FILE  The output file.\n--verbose      Enable verbose"
            " mode.\n"
        )
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_option_list_long_value_unchanged(self):
        # An option list entry whose description exceeds WIDTH must
        # not be wrapped.
        src = (
            "-o FILE  The output file path which is extremely"
            " long and goes well beyond the target width of"
            " seventy-nine characters easily\n"
        )
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_quoted_literal_block_unchanged(self):
        src = "Example::\n\n> quoted line one\n> quoted line two\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_doctest_block_unchanged(self):
        src = ">>> print('hello')\nhello\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_footnote_unchanged(self):
        src = ".. [1] This is a footnote.\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_citation_unchanged(self):
        src = ".. [CIT2023] A citation reference.\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_anonymous_hyperlink_target_unchanged(self):
        src = "__ https://example.com/some/long/path\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_line_block_unchanged(self):
        src = "| First line of verse.\n| Second line of verse.\n"
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_tab_indented_directive_body_unchanged(self):
        src = (
            ".. note::\n"
            "\tThis line is indented with a tab.\n"
            "\tAnother line with a tab.\n"
        )
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)

    def test_sphinx_field_list_indented_unchanged(self):
        # Sphinx-style :param: fields inside a directive body are
        # indented, so they pass through verbatim.
        src = (
            ".. py:function:: foo(x)\n"
            "\n"
            "   :param very_long_parameter_name: This is a long"
            " description that should not be wrapped.\n"
            "   :type very_long_parameter_name: str\n"
        )
        out = self.wrap(src)
        assert out == src
        self.check_all(src, out)
