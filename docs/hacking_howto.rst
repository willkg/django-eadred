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

* PEP-8: http://www.python.org/dev/peps/pep-0008/
* PEP-257: http://www.python.org/dev/peps/pep-0257/
* Use pyflakes. Srsly.

pep8 covers Python code conventions. pep257 covers Python docstring
conventions.

Minor caveats:

* We use Sphinx, so do function definitions like they do:
  `<http://packages.python.org/an_example_pypi_project/sphinx.html#function-definitions>`_.
* Don't kill yourself over 80-character lines, but it is important.
* If you're flummoxed by the conventions, just send me the patch and
  as long as it functionally works, I can do a cleanup pass in a
  later commit.


Git conventions
===============

I encourage good commit messages in a form that works well with git's
various commands. Something like
`<http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>`_. except
that I don't care about verb tense or capitalization and if the commit
message is tied to a bug report, the bug report number should be the
first thing in the first line. Here's the tbaggery example with some
adjustments::

    475. short summary (50 chars or less)

    More detailed explanatory text, if necessary.  Wrap it to about 72
    characters or so.  In some contexts, the first line is treated as
    the subject of an email and the rest of the text as the body.  The
    blank line separating the summary from the body is critical
    (unless you omit the body entirely); tools like rebase can get
    confused if you run the two together.

    Further paragraphs come after blank lines.

    - Bullet points are okay, too

    - Typically a hyphen or asterisk is used for the bullet, preceded
      by a single space, with blank lines in between, but conventions
      vary here

    - Use a hanging indent

Why? Here's the reasons:

* 50 characters or less works well with the various git commands that
  show only the summary line and also on github.
* Having the bug number as the first thing makes it easy to see which
  commits covered which bugs without parsing the commit message. We do
  that a lot ("When did the fix for bug xyz land?").
* Wrapping the subsequent paragraphs allows them to show up nicely in
  git output as well as on github.

Why not the other things? Here's the reasons:

* Capitalization or non-capitalization for a phrase doesn't affect the
  output of git commands or my ability to quickly parse a summary.
* Ditto for verb tense.
* I'm all for ditching convention baggage for things that don't
  matter.


Code documentation conventions
==============================

Documentation in the code is really helpful. Please add comments where
you think it's necessary.

We like to use docstrings for classes, methods and functions. They
should be in reStructuredText format. Something along these lines,
though most of our docstrings aren't as formal or complete::

    def foo(arg1, arg2):
        """Foo does something interesting

        :arg arg1: Controls whether or not to bar
        :arg arg2: Name of the baz to use

        :raises ValueError: If arg2 is not a valid baz.

        :returns: A bat.
        """

The purpose in-code documentation is three-fold:

1. to clarify complex code so it's easier to discern what it's doing
2. to make it clear why the code is doing what it's doing
3. to document any issues the code might have


Building the documentation
==========================

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
