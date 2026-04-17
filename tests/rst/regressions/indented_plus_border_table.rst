Indented ASCII table with ``+`` row prefix, not in literal block
=================================================================

Regression for the nested-list dispatch branch firing on a homemade
ASCII table whose rows begin with ``+`` (not a real RST grid table,
which would use ``|`` for data rows). The table lives inside
indented prose that ends with a single colon (not ``::``), so it's
not a literal block body -- docutils parses it as ad-hoc content in
a block quote -- and the existing literal-block guard doesn't
apply. The dispatcher must leave it verbatim: the rows look like
bullet items (``+ text``) but are inline content of a mangled
table whose shape must be preserved. Requires rows longer than the
target width so that ``_handle_list_run``'s ``fits_verbatim`` guard
doesn't silently mask the bug. Reduced from
``Documentation/admin-guide/pm/amd-pstate.rst`` in the Linux kernel.

Results:

     Open selftest.tbench.csv :

     +-------------------------------------------------+--------------+----------+
     + Governor                                        | Round        | Des-perf |
     +-------------------------------------------------+--------------+----------+
     + amd-pstate-ondemand                             | 1            | 165.329  |
     +-------------------------------------------------+--------------+----------+
     + amd-pstate-ondemand                             | 2            | 166      |
     +-------------------------------------------------+--------------+----------+
