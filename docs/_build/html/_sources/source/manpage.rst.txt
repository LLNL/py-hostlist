py-hostlist
===========

SYNOPSIS
--------

**python cla_hostlist.py [OPTION] ARGS

DESCRIPTION
-----------

py-hostlist is a hostlist utility implemented in Python. It uses regular expressions to manipulate hostlists and perform logic functions between different types of hostlists.

OPTIONS
-------

.. option:: -h, --help

   Display this message.

.. option:: -q, --quiet

   Quiet output (exit non-zero if empty hostlist)

EXAMPLES
--------

1. To expand a hostlist:

   python cla_hostlist.py -e foo[1-5]

The py-hostlist source code and all documentation may be downloaded from <https://github.com/llnl/py-hostlist.git>