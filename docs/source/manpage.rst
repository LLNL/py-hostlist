py-hostlist Man Page
====================

SYNOPSIS
--------

``python cla_hostlist.py [OPTION] ARGS``

DESCRIPTION
-----------

py-hostlist is a hostlist utility implemented in Python. It uses regular expressions to manipulate hostlists and perform logic functions between different types of hostlists.

OPTIONS
-------

.. option:: -h, --help

   Display this message.

.. option:: -q, --quiet

   Quiet output (exit non-zero if empty hostlist).

.. option:: -d, --delimiters

   Set output delimiter (default = ",").

.. option:: -c, --count

   Print the number of hosts.

.. option:: -s, --size

   Output at most N hosts (-N for last N hosts).

.. option:: -e, --expand

   Expand a compressed hostlist.

.. option:: -a, --abbreviate

   Compress an expanded hostlist.

.. option:: -t, --tighten

   Return a hostlist string.

.. option:: -m, --minus

   Subtract all HOSTLIST args from first HOSTLIST.

.. option:: -i, --intersection

   Intersection of all HOSTLIST args.

.. option:: -x, --exclude
   
   Exclude all HOSTLIST args from first HOSTLIST.

.. option:: -X, --xor

   Symmetric difference of all HOSTLIST args.

.. option:: -u, --union

   Union of all HOSTLIST arguments.

.. option:: -n, --nth

   Output the host at index N.

.. option:: -R, --remove

   Remove all occurences of NODE from HOSTLIST.

.. option:: -S, --sort
  
   Return a sorted HOSTLIST.

.. option:: -F, --find

   Output position of HOST in result HOSTLIST.

RESTRICTIONS
------------

For most of the functions, hostlists can be input as any of the following three formats:

   - ``foo1,foo2,foo3,foo4,foo5``

   - ``foo[1-5]`` 

   - ``[foo1,foo2,foo3,foo4,foo5]``

EXAMPLES
--------

1. To expand a hostlist:

   ``python cla_hostlist.py -e foo[1-5]``

2. To set a custom delimiter:

   ``python cla_hostlist.py -d [DELIMITER] foo[1-5]``

3. To see the first N hosts:

   ``python cla_hostlist.py -s [N] foo[1-5]``

4. To exclude a node from a hostlist:

   ``python cla_hostlist.py -x foo[1-5] [EXCLUDED NODE] [EXCLUDED NODE]...``

5. To find the nth host in a hostlist:

   ``python cla_hostlist.py -n [N] foo[1-5]``

6. To remove all occurences of a node from a hostlist:

   ``python cla_hostlist.py -R [NODE] foo[1-5]``

7. To find the position of a specific node:

   ``python cla_hostlist.py -F [NODE] foo[1-50]``



The py-hostlist source code and all documentation may be downloaded from <https://github.com/llnl/py-hostlist.git>