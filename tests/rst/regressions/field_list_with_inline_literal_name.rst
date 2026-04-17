..
    Regression: a field name containing an inline literal
    (``:``p_offset``: ...``) is valid but was excluded by
    _FIELD_LIST_RE's backtick ban. The trailing ``(?:\s|$)`` already
    disambiguates roles, so the ban is unnecessary.
    Found in Linux ``arch/arm64/memory-tagging-extension.rst``.

Some prose paragraph before the field list.

:``p_type``: ``PT_AARCH64_MEMTAG_MTE``
:``p_flags``: 0
:``p_offset``: segment file offset
:``p_vaddr``: segment virtual address, same as the corresponding
  ``PT_LOAD`` segment
:``p_paddr``: 0

Trailing prose paragraph.
