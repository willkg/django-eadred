.. _hacking-howto-chapter:

===============
 Hacking HOWTO
===============

This covers setting up a development environment for developing on
eadred.


Setting up a development environment
====================================

Run::

    $ virtualenv ./venv/
    $ . ./venv/bin/activate
    $ pip install -r requirements-dev.txt
    $ python setup.py develop

This sets up all the required dependencies for development of eadred.

.. Note::

   You don't have to put your virtual environment in ``./venv/``. Feel
   free to put it anywhere.


Coding conventions
==================

We follow the code conventions listed in the `coding conventions page
of the webdev bootcamp guide
<http://mozweb.readthedocs.org/en/latest/coding.html>`_. This covers
all the Python code.

We use git and follow the conventions listed in the `git and github
conventions page of the webdev bootcamp guide
<http://mozweb.readthedocs.org/en/latest/git.html#working-on-projects>`_.


Documentation conventions
=========================

See the `docmentation page in the webdev bootcamp guide
<http://mozweb.readthedocs.org/en/latest/documentation.html>`_ for
documentation conventions.

The documentation is available in HTML and PDF forms at
`<http://elasticutils.readthedocs.org/>`_. This tracks documentation
in the master branch of the git repository. Because of this, it is
always up to date.


Building the docs
=================

The documentation in `docs/` is built with `Sphinx
<http://sphinx.pocoo.org/>`_. To build HTML version of the
documentation, do::

    $ cd docs/
    $ make html


Running the tests
=================

To run the tests, do::

    $ ./run_tests.py

or run it with the python interpreter of your choice::

    $ /path/to/python run_tests.py


Writing tests
=============

Tests are located in ``eadred/tests/``.

We use `nose <https://github.com/nose-devs/nose>`_ for test utilities
and running tests.


Release process
===============

1. Checkout master tip.

2. Update version numbers in ``eadred/_version.py``.

   1. Set ``__version__`` to something like ``0.4``.
   2. Set ``__releasedate__`` to something like ``20120731``.

3. Update ``CONTRIBUTORS``, ``CHANGELOG``, ``MANIFEST.in``.

4. Verify correctness.

   1. Run tests.
   2. Build docs.
   3. Verify all that works.

5. Tag the release::

       $ git tag -a v0.4

6. Push everything::

       $ git push --tags official master

7. Update PyPI::

       $ python setup.py sdist upload

8. Update topic in ``#eadred``, blog post, twitter, etc.
