Indented directive body with YAML-like content
===============================================

Regression for the nested-list dispatch branch firing inside the
body of an indented directive. When a ``.. code-block:: yaml``
directive appears inside a bullet list item body (col 2), the main
dispatch's ``..`` branch doesn't handle it -- it's caught as an
indented line by ``_try_verbatim`` -- and the directive body's
``- name: ...`` lines (YAML sequence items) land individually at
the dispatch loop, where they are bullet-shaped and at a block
boundary (blank line above). The guard must see the indented
directive marker above the blank and treat its body as opaque.
Reduced from Ansible's porting guides.

* Conditionals - due to mitigation of security issue CVE-2023-5764
  in ansible-core 2.14.12, conditional expressions with embedded
  template blocks can fail when the embedded template consults
  untrusted data.

  .. code-block:: yaml

     - name: task with a module result (always untrusted by Ansible)
       shell: echo "hi mom"
       register: untrusted_result

     - name: securely access untrusted values directly as Jinja variables
       assert:
         that: '"hi mom" is in untrusted_result.stdout'
