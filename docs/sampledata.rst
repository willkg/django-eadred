========================
 Generating sample data
========================

Running the cli
===============

To generate sample data, do this::

    $ ./manage.py generatedata

That will go through all your ``INSTALLED_APPS`` looking for modules
named ``sampledata`` and executing the ``generate_data`` method in
each.

That's pretty much the gist of it.


Creating a sampledata module
============================

Before you can generate data, you need to write a ``generate_data``
function.

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
``generate_data``.

Here's an example::

    def generate_data():
        pass

In that function, you do whatever you want to do to generate data.


Example 1: Load a fixture
=========================

This ``generate_data`` function loads a fixture (ab)using the Django
loaddata command::

    from django.core.management.commands import loaddata

    def generate_data():
        cmd = loaddata.Command()
        cmd.loaddata('mydata.json')


Example 2: Generate data with model makers
==========================================

This example has a rough model maker for the Record model and creates
10 Records using it::

    import datetime

    from someproject.someapp.models import Record


    def record(**kwargs):
        rec = Record(**kwargs)
        rec.save()
        return rec

    def generate_sampledata():
        now = datetime.datetime.now()

        # Creates 10 records, each on a new day.
        for i in range(10):
            record(created=now - datetime.timedelta(days=i),
                   message='Lorem ipsum %d' % i)
