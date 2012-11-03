========
 README
========

eadred is a Django-app for generating sample data.

Why? Here are the use cases we're solving:

**Use Case 1: Contributors**

    Mildred wants to contribute to your Django project, but your
    Django project is non-trivial and out of the box it's not very
    usable because it needs data.

    However, you're using eadred, so in your setup documentation, you
    have a one-liner that generates all the sample data Mildred needs
    to start hacking immediately.

**Use Case 2: Bootstrapping**

    Willhelm wants to set up an instance of your Django project. It
    requires certain non-trivial initial data to be in place before it
    works.

    However, you're using eadred, so in your setup documentation, you
    have a one-liner that generates all the initial data needed.

**Use Case 3: Large amounts of random data**

    Phylida is a hacker on your Django project and trying to fix bugs
    with a section of code that requires large amounts of data---say
    it's one of those things that graphs data sets or something.

    You're using eadred, so it's a one-liner to generate a large set
    of initial data.


"Wait, use cases 1 and 2 are easily solved with Django and fixtures!"

I think fixtures are good for specific use cases where your models
aren't changing and you have some contributor who likes entering in
data to build the initial fixtures. Having said that, I don't use
fixtures.

eadred allows you to programmatically generate the data using model
makers, factories, fixtures, random seeds---whatever your needs are.

Additionally, eadred provides library functions to make generating
data easier.


Project details
===============

Code:
    http://github.com/willkg/django-eadred

Documentation:
    http://django-eadred.rtfd.org/

Issue tracker:
    https://github.com/willkg/django-eadred/issues

License:
    BSD 3-clause; see LICENSE file
