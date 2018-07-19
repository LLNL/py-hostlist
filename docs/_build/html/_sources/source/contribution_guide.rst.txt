==================
Contribution Guide
==================

This guide is intended for developers or administrators who want to contribute a new feature or bugfix to py-hostlist. It assumes that you have at least some familiarity with Git VCS and GitHub. The guide will show a few examples of contributing workflows and discuss the granularity of pull-requests (PRs). It will also discuss the tests your PR must pass in order to be accepted into py-hostlist.

First, what is a PR? Quoting `Bitbucket's tutorials <https://www.atlassian.com/git/tutorials/making-a-pull-request/>`_:

	Pull requests are a mechanism for a developer to notify team members that they have **completed a feature**. The pull request is more than just a notification—it’s a dedicated forum for discussing the proposed feature.

Important is **completed feature**. The changes one proposes in a PR should correspond to one feature/bugfix/extension/etc. One can create PRs with changes relevant to different ideas, however reviewing such PRs becomes tedious and error prone. If possible, try to follow the **one-PR-one-package/feature** rule.


----------------------
Continuous Integration
----------------------

py-hostlist uses `Travis CI <https://travis-ci.org/LLNL/py-hostlist>`_ for Continuous Integration testing. This means that every time you submit a pull request, a series of tests will be run to make sure you didn't accidentally introduce any bugs into py-hostlist. **Your PR will not be accepted until it passes all of these tests.** While you can certainly wait for the results of these tests after submitting a PR, we recommend that you run them locally to speed up the review process.

.. note::

   Oftentimes, Travis will fail for reasons other than a problem with your PR.
   For example, apt-get, pip, or homebrew will fail to download one of the
   dependencies for the test suite, or a transient bug will cause the unit tests
   to timeout. If Travis fails, click the "Details" link and click on the test(s)
   that is failing. If it doesn't look like it is failing for reasons related to
   your PR, you have two options. If you have write permissions for the py-hostlist
   repository, you should see a "Restart job" button on the right-hand side. If
   not, you can close and reopen your PR to rerun all of the tests. If the same
   test keeps failing, there may be a problem with your PR. If you notice that
   every recent PR is failing with the same error message, it may be that Travis
   is down or one of py-hostlist's dependencies put out a new release that is causing
   problems. If this is the case, please file an issue.

If you take a look in ``py-hostlist/.travis.yml``, you'll notice that we test
against Python 2.7, and 3.3-3.7 on macOS. We currently perform unit testing:

Unit tests ensure that core py-hostlist features like expand or compress_range are working as expected. If your PR only adds new packages or modifies existing ones, there's very little chance that your changes could cause the unit tests to fail. However, if you make changes to py-hostlist's core libraries, you should run the unit tests to make sure you didn't break anything.

To run the unit tests, use:

.. code-block:: console

   $ python py-hostlist/unittest_hostlist.py

It should only take a few seconds to complete. If you know you are only modifying a single feature, you can run a single unit test at a time:

.. code-block:: console

   $ python py-hostlist/unittest_hostlist.py TestHostlistMethods.test_expand

-------------
Git Workflows
-------------

py-hostlist is still in the alpha stages of development. Most of our users run off of
the develop branch, and fixes and new features are constantly being merged. So
how do you keep up-to-date with upstream while maintaining your own local
differences and contributing PRs to py-hostlist?

^^^^^^^^^
Branching
^^^^^^^^^

The easiest way to contribute a pull request is to make all of your changes on new branches. Make sure your ``develop`` is up-to-date and create a new branch off of it:

.. code-block:: console

   $ git checkout develop
   $ git pull upstream develop
   $ git branch <descriptive_branch_name>
   $ git checkout <descriptive_branch_name>

Here we assume that the local ``develop`` branch tracks the upstream develop branch of py-hostlist. This is not a requirement and you could also do the same with remote branches. But for some it is more convenient to have a local branch that tracks upstream.

Normally we prefer that commits pertaining to a package ``<package-name>`` have a message ``<package-name>: descriptive message``. It is important to add descriptive message so that others, who might be looking at your changes later would understand the rationale behind them.

Now, you can make your changes while keeping the ``develop`` branch pure.
Edit a few files and commit them by running:

.. code-block:: console

   $ git add <files_to_be_part_of_the_commit>
   $ git commit --message <descriptive_message_of_this_particular_commit>

Next, push it to your remote fork and create a PR:

.. code-block:: console

   $ git push origin <descriptive_branch_name> --set-upstream

GitHub provides a `tutorial <https://help.github.com/articles/about-pull-requests/>`_
on how to file a pull request. When you send the request, make ``develop`` the
destination branch.