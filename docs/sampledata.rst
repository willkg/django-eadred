========================
 Generating sample data
========================

.. contents::
   :local:


Creating a generate_sampledata function
=======================================

Before you can generate data, you need to write a
``generate_sampledata`` function for every Django app that you want to
generate sampledata.

For example, say you had a Django project named `testproject` with a
directory structure like this::

    testproject/
    |- __init__.py
    |- settings.py
    |
    |- testapp/
       |- __init__.py

In the ``settings.py`` file you have ``INSTALLED_APPS`` set like this::

    INSTALLED_APPS = ['testproject.testapp']

That way ``testproject.testapp`` is a valid Django app in your Django
project.

In the ``testapp/`` directory, create a file named ``sampledata.py``.

In the ``sampledata.py`` file, create a function named
``generate_sampledata``.

Here's an example::

    def generate_sampledata(options):
        pass

In that function, you do whatever you want to do to generate data.


Options
=======

The `options` argument holds the options that the OptionParser that
Django uses to parse the command line arguments. Thus it has the
standard options that are passed to every Django command:

* `settings`
* `pythonpath`
* `verbosity`
* `traceback`

Most of those probably aren't useful, but `verbosity` might be.

Additionally, you can use the `with` keyword argument to pass
additional parameters which will get pulled out and added to the
`options` dict.

For example::

    def generate_sampledata(options):
        print options.get('foo')

If you do this::

    $ ./manage.py generatedata --with=foo=bar

it'll print::

    bar


Running ./manage.py generatedata
================================

General use
-----------

To generate sample data, do this::

    $ ./manage.py generatedata

That will go through all your ``INSTALLED_APPS`` looking for modules
named ``sampledata`` and executing the ``generate_sampledata`` method
in each.


Generating data in specified apps
---------------------------------

Say you had a bunch of apps in your Django project that have
sampledata modules, but you only want to generated data in one of
them. You can specify the apps you want to generate data in on the
command line::

    # All apps
    $ ./manage.py generatedata

    # Only app1
    $ ./manage.py generatedata app1

    # Only app1 and app2
    $ ./manage.py generatedata app1 app2


Passing arguments
-----------------

You can also pass arguments to the ``generate_sampledata`` functions
using the `with` keyword argument.

Examples::

    # Passes {'fixtures': True} to options
    $ ./manage.py generatedata --with=fixtures

    # Passes {'type': 'random'} to options
    $ ./manage.py generatedata --with=type=random

    # Passes {'type': 'random', 'seed': '1024'} to options.
    $ ./manage.py generatedata --with=type=random --with=seed=1024

You can have as many as you like---each will get parsed out as a
separate key or key/val parameter.


Recipes
=======

Example 1: Load a fixture
-------------------------

This ``generate_sampledata`` function loads a fixture (ab)using the Django
loaddata command::

    from django.core.management.commands import loaddata

    def generate_sampledata(options):
        cmd = loaddata.Command()
        cmd.execute('mydata.json')


Run it like this::

    $ ./manage.py generatedata


Example 2: Generate data with model makers
------------------------------------------

This example has a rough model maker for the Record model. Also, it
allows the user to specify how many records he/she wants to create
using the `count` parameter::

    import datetime
    from someproject.someapp.models import Record

    def record(**kwargs):
        rec = Record(**kwargs)
        rec.save()
        return rec

    def generate_sampledata(options):
        count = options.get('count', '10')
        count = int(count)

        now = datetime.datetime.now()

        # Creates count number of records, each on a new day.
        for i in range(count):
            record(created=now - datetime.timedelta(days=i),
                   message='Lorem ipsum %d' % i)


Run it like this::

    $ ./manage.py generatedata
    $ ./manage.py generatedata --with=count=20

