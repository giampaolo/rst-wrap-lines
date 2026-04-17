..
    Regression: ``*  text`` (two spaces) has text column 3; a
    bullet-shaped line at col 2 parses as block_quote. Normalizing
    the prefix to one space shifted the column to 2 and turned that
    block_quote into a nested list item, changing the doctree.
    Only triggers when the item is re-wrapped. Found in Ansible
    ``community/collection_contributors/collection_reviewing.rst``.

Intro.

*  Outer item one. This sentence is long enough that it will be re-wrapped by the tool at width 79.
*  Outer item two. This one is also long enough to be re-wrapped by the tool when the width is 79 characters.

  * Nested-looking bullet at column 2 -- parsed as a block_quote because its indent is below the outer item's text column (3).

*  Outer item three, also long enough to be re-wrapped by the tool when the width is 79 characters.

Trailing paragraph.
