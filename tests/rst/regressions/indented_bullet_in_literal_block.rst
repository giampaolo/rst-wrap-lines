Indented bullet inside literal block
====================================

Regression: nested-list dispatch fires on an indented line that
looks like a bullet but lives inside a ``::`` literal block --
content is opaque and must pass through verbatim. Reduced from
CPython's ``Doc/howto/gdb_helpers.rst`` (``gdb``'s ``info threads``
output with ``* 1 Thread ...`` marking the current thread).

The ``info threads`` command will give you a list of the threads within the
process, and you can use the ``thread`` command to select a different one::

        (gdb) info threads
          105 Thread 0x7fffefa18710 (LWP 10260)  sem_wait () at ../nptl/sysdeps/unix/sysv/linux/x86_64/sem_wait.S:86
          104 Thread 0x7fffdf5fe710 (LWP 10259)  sem_wait () at ../nptl/sysdeps/unix/sysv/linux/x86_64/sem_wait.S:86
        * 1 Thread 0x7ffff7fe2700 (LWP 10145)  0x00000038e46d73e3 in select () at ../sysdeps/unix/syscall-template.S:82

Prose after the literal block.
