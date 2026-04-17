Tab-indented nested bullets left verbatim
==========================================

Regression: ``_handle_list_run``'s ``visually_attached`` guard
measures indent with ``lstrip(' ')`` (no tabs), so a tab-nested
child reads as indent 0 and "not attached"; wrapping a long
parent to two lines then flips docutils' parse of the block.
Until that measurement is fixed, the nested-list dispatch fires
only on space-indented content. Reduced from Linux's
``Documentation/misc-devices/xilinx_sdfec.rst``.

Monitor for Interrupts
----------------------

	- Use the poll system call to monitor for an interrupt. The poll system call waits for an interrupt to wake it up or times out if no interrupt occurs.
	- On return Poll ``revents`` will indicate whether stats and/or state have been updated
		- ``POLLPRI`` indicates a critical error and the user should use :c:macro:`XSDFEC_GET_STATUS` and :c:macro:`XSDFEC_GET_STATS` to confirm
		- ``POLLRDNORM`` indicates a non-critical error has occurred and the user should use  :c:macro:`XSDFEC_GET_STATS` to confirm
