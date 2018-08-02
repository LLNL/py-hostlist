.. py-hostlist documentation master file, created by
   sphinx-quickstart on Thu Jul 12 14:48:48 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

py-hostlist
=======================================

py-hostlist processes slurm-style hostlist strings and can return those strings in manipulated fashion.

Get py-hostlist from the `github repository <https://github.com/LLNL/py-hostlist>`_:

.. code-block:: console

   $ git clone https://github.com/llnl/py-hostlist.git
   $ cd py-hostlist

From here, build and install the package on your machine:

.. code-block:: console

   $ python setup.py sdist bdist_wheel
   $ pip install dist/py_hostlist-0.0.1.dev0-py2.py3-none-any.whl

Now you can start using it!

.. code-block:: console

   $ hostlist -h

.. toctree::
   :maxdepth: 2
   :caption: Basics

   source/features
   source/basic_usage

.. toctree::
   :maxdepth: 2
   :caption: Reference

   source/method_reference
   source/manpage

.. toctree::
   :maxdepth: 2
   :caption: Contributing

   source/contribution_guide
   source/developer_guide
   source/adding_unit_tests

.. toctree::
   :maxdepth: 2
   :caption: AutoDocs

   source/hostlist

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
