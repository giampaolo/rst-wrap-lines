# RST rules

This file documents docutils' actual parsing behaviour at the
boundary cases where intuition is unreliable. Each rule is paired
with a minimal probe (a few `publish_doctree()` / `parse()` calls)
that establishes the behaviour empirically.

The tool's transformations must respect these rules — getting one
wrong breaks the doctree-equality invariant in `TestDocutils`.

## Directive marker

A line of the form `.. NAME::` is parsed as a directive **only** when
`::` is followed by whitespace or end-of-line. Any non-whitespace
character immediately after `::` makes docutils fall back to parsing
the whole block as a `comment` node.

| Source | Parsed as |
| --- | --- |
| `.. note::` | directive (empty body) |
| `.. note:: hello` | directive |
| `.. note::hello` | comment |
| `` .. note:::ref:`x` `` | comment |
| `.. note::: hello` | comment |
| `.. note:::: hello` | comment |
| `.. py:function::` | directive (with domain) |
| `` .. py:function:::ref:`x` `` | comment |
| `.. fakething::` | directive (unknown name, but well-formed) |
| `.. note: not a directive` | comment (single colon) |
| `..note::` | paragraph (no space between `..` and name) |

Probe:

```python
import docutils.utils, docutils.frontend, docutils.parsers.rst, docutils.nodes

def kind(s):
    settings = docutils.frontend.OptionParser(
        components=(docutils.parsers.rst.Parser,)
    ).get_default_values()
    settings.report_level = 5
    doc = docutils.utils.new_document("<x>", settings)
    docutils.parsers.rst.Parser().parse(s + "\n", doc)
    return [
        c.tagname
        for c in doc.children
        if not isinstance(c, docutils.nodes.system_message)
    ]

for src in [
    ".. note::",
    ".. note:: hello",
    ".. note::hello",
    ".. note:::ref:`x`",
    ".. note::: hello",
    ".. note:::: hello",
    ".. py:function::",
    ".. py:function:::ref:`x`",
    ".. fakething::",
    ".. note: not a directive",
    "..note::",
]:
    print(repr(src), "->", kind(src))
```

Implication for the tool: `_DIRECTIVE_RE` must anchor the trailing
`::` with `(?=\s|$)`. Without that lookahead, malformed markers
like `.. note:::ref:` are misclassified as directives, the body is
re-wrapped, and the comment node's text mutates — breaking the
doctree invariant. The bug was found in
`Documentation/userspace-api/media/v4l/mmap.rst` in the Linux
kernel docs (regression:
`tests/rst/regressions/malformed_directive_parsed_as_comment.rst`).
