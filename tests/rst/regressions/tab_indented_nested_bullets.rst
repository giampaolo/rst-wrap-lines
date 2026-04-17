..
    Regression: ``_handle_list_run``'s ``visually_attached`` guard
    uses ``lstrip(' ')`` (no tabs), so tab-nested children read as
    indent 0 and "not attached"; wrapping a long parent to two
    lines then flips the doctree. Dispatch fires on spaces only
    until the measurement is fixed. Reduced from Linux's
    ``misc-devices/xilinx_sdfec.rst``.

Monitor for Interrupts
----------------------

	- Use the poll system call to monitor for an interrupt. The poll system call waits for an interrupt to wake it up or times out if no interrupt occurs.
	- On return Poll ``revents`` will indicate whether stats and/or state have been updated
		- ``POLLPRI`` indicates a critical error and the user should use :c:macro:`XSDFEC_GET_STATUS` and :c:macro:`XSDFEC_GET_STATS` to confirm
