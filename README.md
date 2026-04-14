# rst-wrap-lines

A command-line tool that wraps prose paragraphs of `.rst` (reStructured Text)
files to a maximum line length.

Only prose paragraphs and list items are re-wrapped. Everything else
(directives, literal blocks, tables, section underlines, comments, indented
blocks) is passed through byte-identical. If a file is already clean, the tool
produces a zero-byte diff.

## Installation

```
pip install rst-wrap-lines
```

## Usage

```bash
rst-wrap-lines docs/*.rst
rst-wrap-lines docs/                # whole dir, recursive
rst-wrap-lines --check docs/*.rst
rst-wrap-lines --width 80 foo.rst
```

Options:

- `-w`, `--width` — maximum line length (default: 79)
- `--check` — exit with code 1 if any file would be changed; do not write
- `--diff` — print a unified diff instead of writing files

## What gets wrapped

- Prose paragraphs
- List items (bullet and enumerated), including multi-line continuations
- Bodies of prose-body directives (`.. note::`, `.. warning::`,
  `.. versionadded::`, `.. class::`, etc.)
- Double spaces in prose are removed (e.g. `hello  world` → `hello world`),
  even when the paragraph already fits within the target width

## What is left untouched

- Literal blocks (`.. code-block::`, `::` blocks)
- Tables (grid and simple)
- Section titles and underlines
- Comments, hyperlink targets, substitution definitions
- Field lists (`:param foo:`, `:type bar:`)
- Definition list terms and their bodies
- Option list items (`-x`, `--foo`)
- Block quotes

Inline RST constructs that contain internal whitespace (`` ``like this`` ``,
``:role:`display <target>` ``, ``*emphasis*``, ``**bold**``, etc.) are treated
as atomic tokens and never broken across lines. Spaces inside inline constructs
are left intact.

## Tested against CPython docs

The test suite runs against all ~600 `.rst` files in the
[CPython documentation](https://github.com/python/cpython/tree/main/Doc)
and verifies:

- **Idempotency** — running the tool twice produces the same output as
  running it once.
- **Width** — no tool-produced line exceeds the target width (verbatim
  passthrough of already-long source lines is allowed).
- **No double spaces** — no tool-produced prose line contains a bare
  double space.
- **Document tree invariant** — parsing the original and the wrapped
  file with [docutils](https://docutils.sourceforge.io/) produces
  identical document trees (after normalising intra-node whitespace).
  This confirms that rewrapping prose never alters headings, directives,
  code blocks, hyperlinks, or any other structural element.

## Development

```
make test
make lint-all
make fix-all
```

## License

MIT
