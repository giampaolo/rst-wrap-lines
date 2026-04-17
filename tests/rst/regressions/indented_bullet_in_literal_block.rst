..
    Regression: nested-list dispatch fires on an indented bullet-
    looking line inside a ``::`` literal block. Reduced from
    CPython's ``Doc/howto/gdb_helpers.rst`` (``gdb``'s ``info
    threads`` output).

The ``info threads`` command will give you a list of the threads within the
process, and you can use the ``thread`` command to select a different one::

        (gdb) info threads
          105 Thread 0x7fffefa18710 (LWP 10260)  sem_wait () at ../nptl/sysdeps/unix/sysv/linux/x86_64/sem_wait.S:86
        * 1 Thread 0x7ffff7fe2700 (LWP 10145)  0x00000038e46d73e3 in select () at ../sysdeps/unix/syscall-template.S:82

Prose after.
