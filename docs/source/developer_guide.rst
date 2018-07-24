===============
Developer Guide
===============

This guide is intended for people who want to work on py-hostlist itself. 

Overview
--------

py-hostlist is designed with two separate roles in mind:

 1. **Users**, who need to use the hostlist tool without knowing all of the details about how it is built.

 2. **Developers** who work on py-hostlist, add new features, and try to make the jobs of users easier.

As you might expect, there are many types of users with different levels of sophistication, and py-hostlist is designed to accommodate both simple and complex use cases for this tool. A user who only knows that he needs a small task, like expanding a hostlist, should be able to type something simple like ``python cla_hostlist.py -e foo[1-4]`` and get a result in return.

Directory Structure
-------------------

Here is a high level view of py-hostlist's directory structure:

.. code-block:: none

      dist/                       <- packaged build

      docs/
        Makefile
        conf.py
        index.rst
        make.bat
        build/                    <- HTML pages
        source/                   <- ReadTheDocs pages
          .doctrees/

      hostlist/
        __init__.py
        cla_hostlist.py           <- command-line arguments
        hostlist.py               <- main features and methods
        unittest_hostlist.py      <- unit tests for hostlist.py

Code Structure
--------------

For an overview of the various Python modules in py-hostlist, please see the Method Reference section.