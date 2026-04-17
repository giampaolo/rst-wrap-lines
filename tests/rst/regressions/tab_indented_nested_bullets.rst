Tab-indented nested bullets left verbatim
==========================================

Regression for the nested-list dispatch branch firing on
tab-indented content. The Linux kernel (and other old-school
projects) indent bullets with hard tabs; docutils expands tabs to
8 cols before parsing, but ``_handle_list_run``'s
``visually_attached`` guard measures indent as ``len - len.lstrip(' ')``
(spaces only), so a tab-nested bullet reads as ``indent = 0`` and
the guard mis-reports "not attached". Wrapping a long parent item
into two lines under those conditions flips docutils' parse of
``<list_item><definition_list>...`` into
``<list_item><paragraph>...<block_quote><bullet_list>...``, which
breaks the doctree invariant.

Until the measurement bug in ``visually_attached`` is fixed, the
dispatch branch only fires on space-indented nested content;
tab-indented content stays verbatim (pre-fix behaviour).
Reduced from ``Documentation/misc-devices/xilinx_sdfec.rst`` in
the Linux kernel.

Monitor for Interrupts
----------------------

	- Use the poll system call to monitor for an interrupt. The poll system call waits for an interrupt to wake it up or times out if no interrupt occurs.
	- On return Poll ``revents`` will indicate whether stats and/or state have been updated
		- ``POLLPRI`` indicates a critical error and the user should use :c:macro:`XSDFEC_GET_STATUS` and :c:macro:`XSDFEC_GET_STATS` to confirm
		- ``POLLRDNORM`` indicates a non-critical error has occurred and the user should use  :c:macro:`XSDFEC_GET_STATS` to confirm
