Nested list items wrapped
=========================

Regression for nested bullet lists -- parent line, blank line, then
indented child bullets -- where over-width child items were passed
through verbatim because the main dispatch's indented-line
passthrough branch caught them before the list-item branch could
see them. Reduced from a real-world block in the psutil changelog.

The buggy behaviour passes the input through unchanged, so the
integration assertions in ``tests/test_integration.py`` silently
accept it (doctree unchanged because output == source; the width
assertion allows over-width lines that already existed in the
source). The real catch lives in the paired unit test
``tests/test_lists.py::TestListItems::test_nested_list_after_blank_wrapped``.

- Split docs into multiple sections:

  - :doc:`/alternatives <alternatives>`: list of alternative Python libraries and tools that overlap with psutil.
  - :doc:`/credits <credits>`: list contributors and donors (was old ``CREDITS`` in root dir).
  - :doc:`/migration <migration>`: explain how to migrate to newer psutil
    versions that break backward compatibility.
