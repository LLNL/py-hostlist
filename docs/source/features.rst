========
Features
========

This is a high-level overview of features that make up py-hostlist, a Python implementation of a hostlist manager.

-------------------------
Using Regular Expressions
-------------------------

py-hostlist utilizes the `re <https://docs.python.org/2/library/re.html>`_ package to look for certain types of hostlist strings to manipulate. Once it matches with a hostlist string, it breaks up the expression into certain control groups with which it can perform a number of operations on. In general, input hostlist strings are broken up into three control groups:

1. the host name

2. the range of nodes contained by the host

3. any suffixes or domains appended to the hostlist

-------------------
String Manipulation
-------------------

After an input string is matched, the control groups are cast to string variables, where they can be stripped of characters such as brackets, dashes, and commas in order to perform necessary operations, such as expanding or compressing a list.

---------------------
Different Input Types
---------------------

py-hostlist is flexible with the types of input passed into its methods. Both lists and strings can be passed into each of the operations that it supports. For example, the compress method accepts the following list input:

``['node1','node2','node3','node4']``

as well as a simple string:

``'node1,node2,node3,node4'``

Both will return the following: ``node[1-4]``

py-hostlist achieves this functionality by checking the type of input before it attempts to do any manipulations/operations.