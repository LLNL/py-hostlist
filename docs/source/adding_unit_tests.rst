=================
Adding Unit Tests
=================

This guide is intended for anyone who wants to add unit tests for any new features
added to py-hostlist.

Python's Unit Test Structure
----------------------------

First, some background on Python's unit test structure. py-hostlist utilizes the `unittest <https://docs.python.org/2/library/unittest.html>`_ unit testing framework in order to test its methods. All of the methods consist of testing the equality of two strings: the *expected* value and the *actual* value. An example:

.. code-block:: none

    def test_expand(self):
        expected = 'quartz4,quartz5,quartz6,quartz7,quartz8'
        test = hl.expand('quartz[4-8]')
        self.assertEqual(test, expected)

``def test_expand(self)`` defines the method name. In this case, we are just testing the expand method; hence, the name ``test_expand``. If we were to test something specific about expand, such as expanding with multiple ranges, than the method name should reflect it, i.e. something like ``test_expand_multi_range``.

.. note::

    All of the test methods used must start with the word ``test``. This informs the test runner about which methods represent tests.

``expected = 'quartz4,quartz5,quartz6,quartz7,quartz8'`` is the expected value we expect to get from running the ``expand`` method.

``test = hl.expand('quartz[4-8]')`` stores a string in ``test`` resulting from calling hostlist's ``expand`` method on the hostlist ``quartz[4-8]``.

.. note::

    The hostlists passed into hostlist's methods are *strings*. Although the command-line tool does not require quotes around its arguments, the unit test file does.

``self.assertEqual(test, expected)`` compares the variables ``expected`` and ``test`` and ensures that they are equal.

How to Add a Unit Test to unittest_hostlist
-------------------------------------------

In order to add a unit test to py-hostlist, use the following steps:

1. Give your test method a name which: **1)** includes the name of the Python method you are testing, and **2)** clearly describes what it is testing.

2. Define the expected value you are looking to get and store it in the variable ``expected``.

3. Call the method from within py-hostlist using ``hl.<your_method>(<value>)`` and store it in the variable ``test``.

4. Call ``self.assertEqual(test, expected)`` to compare the two values. If the test fails, it will most likely be because the strings are not equal, in which case you will see the string returned by both variables to compare.

Running Your Unit Tests
-----------------------

When you push your new test methods to GitHub, `Travis CI <https://travis-ci.org/LLNL/py-hostlist>`_ will automatically run the unit test script to check for successes or failures. However, to run your test methods locally, just run the following command from the ``hostlist`` directory:

``python unittest_hostlist.py``

If you just want to run your specific test method, you can use the following command:

``python unittest_hostlist.py TestHostlistMethods.<your_method_name>``
