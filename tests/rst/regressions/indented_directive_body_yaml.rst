Indented directive body with YAML-like content
===============================================

Regression: nested-list dispatch fires inside an indented
``.. code-block:: yaml`` body. The indented marker is caught by
``_try_verbatim`` and never reaches the directive handler, so the
``- name: ...`` YAML items are dispatched individually and look
like bullets preceded by a blank. Reduced from Ansible's porting
guides.

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
