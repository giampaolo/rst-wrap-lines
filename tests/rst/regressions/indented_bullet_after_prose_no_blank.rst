Indented bullet right after indented prose, no blank line
==========================================================

Regression for the nested-list dispatch branch firing on an
indented bullet that follows an indented prose line with no blank
separator. Docutils parses the whole run as a single paragraph
(the ``*`` characters are inline text, not list markers), but the
old predicate saw ``out[-1]`` as non-blank-indented and treated
that as a block boundary for the indented-bullet branch -- which
turned the paragraph into ``<block_quote> + <bullet_list>`` in
the output doctree. The guard must only fire after a blank line.
Reduced from ``doc/en/backwards-compatibility.rst`` in pytest
(where the enclosing construct is an enum list, not a directive).

a) trivial: APIs that trivially translate to the new mechanism.

   For the PR to mature from POC to acceptance, it must contain:
   * Setup of deprecation errors/warnings that help users fix and port their code. If it is possible to introduce a deprecation period under the current series, before the true breakage, it should be introduced in a separate PR and be part of the current release stream.
   * Detailed description of the rationale and examples on how to port code in ``doc/en/deprecations.rst``.
