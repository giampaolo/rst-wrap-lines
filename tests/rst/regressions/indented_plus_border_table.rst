Indented ASCII table with ``+`` row prefix, not in literal block
=================================================================

Regression: nested-list dispatch fires on a homemade ASCII table
whose rows begin with ``+`` (not an RST grid table, which uses
``|`` for data). The intro ends with a single ``:`` (not ``::``),
so the opaque-context guard doesn't apply. Rows must exceed the
target width, else ``_handle_list_run``'s ``fits_verbatim`` masks
the bug. Reduced from Linux's
``Documentation/admin-guide/pm/amd-pstate.rst``.

Results:

     Open selftest.tbench.csv :

     +-------------------------------------------------+--------------+----------+
     + Governor                                        | Round        | Des-perf |
     +-------------------------------------------------+--------------+----------+
     + amd-pstate-ondemand                             | 1            | 165.329  |
     +-------------------------------------------------+--------------+----------+
     + amd-pstate-ondemand                             | 2            | 166      |
     +-------------------------------------------------+--------------+----------+
