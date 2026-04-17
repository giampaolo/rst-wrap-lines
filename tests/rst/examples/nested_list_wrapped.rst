..
    Nested bullet list (parent + blank + indented children) whose
    over-width children must be wrapped. Integration assertions
    silently accept the buggy verbatim output, so the real catch
    is the paired unit test
    ``test_nested_list_after_blank_wrapped``. Reduced from the
    psutil changelog.

- Split docs into multiple sections:

  - :doc:`/alternatives <alternatives>`: list of alternative Python libraries and tools that overlap with psutil.
  - :doc:`/credits <credits>`: list contributors and donors (was old ``CREDITS`` in root dir).
  - :doc:`/migration <migration>`: explain how to migrate to newer psutil
    versions that break backward compatibility.
