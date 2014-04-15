import os
import random
from itertools import count

try:
    from django.utils.six import text_type
except ImportError:
    text_type = unicode


def get_file(fn):
    """Returns file contents in unicode as list."""
    fn = os.path.join(os.path.dirname(__file__), 'data', fn)
    f = open(fn, 'rb')
    lines = [line.decode('utf-8').strip() for line in f.readlines()]
    return lines


LOREM = get_file('lorem_ipsum.txt')
ENGLISH_MONARCHS = get_file('english_monarchs.txt')
DOMAINS = get_file('domains.txt')


_unique_counter = count()


def reset_counter():
    global _unique_counter
    _unique_counter = count()


def make_unique(gen):
    """Wraps a generator to uniquify strings by appending counter

    :arg gen: the generator to wrap

    Example::

        from eadred.helpers import name_generator, make_unique

        gen = make_unique(name_generator())
        for i in range(50):
            mymodel = SomeModel(name=gen.next())
            mymodel.save()


    Example 2:

    >>> gen = make_unique(name_generator(['alice', 'jane', 'harry']))
    >>> gen.next()
    u'alice0'
    >>> gen.next()
    u'harry1'
    >>> gen.next()
    u'jane2'

    """
    while True:
        yield next(gen) + text_type(next(_unique_counter))


def name_generator(names=None):
    """Creates a generator for generating names.

    :arg names:

        list or tuple of names you want to use; defaults to ENGLISH_MONARCHS

    :returns: generator for names

    Example::

        from eadred.helpers import name_generator

        gen = name_generator()
        for i in range(50):
            mymodel = SomeModel(name=gen.next())
            mymodel.save()


    Example 2:

    >>> gen = name_generator()
    >>> gen.next()
    u'James II'
    >>> gen.next()
    u'Stephen of Blois'
    >>> gen.next()
    u'James I'

    .. Note::

       This gives full names for a "name" field. It's probably not
       useful for broken down name fields like "firstname",
       "lastname", etc.

    """
    if names is None:
        names = ENGLISH_MONARCHS

    while True:
        yield text_type(random.choice(names))


def email_generator(names=None, domains=None, unique=False):
    """Creates a generator for generating email addresses.

    :arg names: list of names to use; defaults to ENGLISH_MONARCHS
        lowercased, ascii-fied, and stripped of whitespace

    :arg domains: list of domains to use; defaults to DOMAINS

    :arg unique: True if you want the username part of the email
        addresses to be unique

    :returns: generator

    Example::

        from eadred.helpers import email_generator

        gen = email_generator()
        for i in range(50):
            mymodel = SomeModel(email=gen.next())
            mymodel.save()


    Example 2:

    >>> gen = email_generator()
    >>> gen.next()
    'eadwig@example.net'
    >>> gen.next()
    'henrybeauclerc@mail1.example.org'
    >>> gen.next()
    'williamrufus@example.com'

    """
    if names is None:
        names = [name.encode('ascii', 'ignore').lower().replace(b' ', b'')
                 for name in ENGLISH_MONARCHS]
    if domains is None:
        domains = DOMAINS

    if unique:
        uniquifyer = lambda: str(next(_unique_counter))
    else:
        uniquifyer = lambda: ''

    while True:
        yield '{0}{1}@{2}'.format(
            random.choice(names), uniquifyer(), random.choice(domains))


def sentence_generator(sentences=None):
    """Creates a generator for generating sentences.

    :arg sentences: list or tuple of sentences you want to use;
        defaults to LOREM

    :returns: generator

    Example::

        from eadred.helpers import sentence_generator

        gen = sentence_generator()
        for i in range(50):
            mymodel = SomeModel(summary=gen.next())
            mymodel.save()

    """
    if sentences is None:
        sentences = LOREM
    while True:
        yield random.choice(sentences)


def paragraph_generator(sentences=None):
    """Creates a generator for generating paragraphs.

    :arg sentences: list or tuple of sentences you want to use;
        defaults to LOREM

    :returns: generator

    Example::

        from eadred.helpers import paragraph_generator

        gen = paragraph_generator()
        for i in range(50):
            mymodel = SomeModel(description=gen.next())
            mymodel.save()

    """
    if sentences is None:
        sentences = LOREM

    while True:
        # Paragraph consists of 1-7 sentences.
        paragraph = [random.choice(sentences)
                     for num in range(random.randint(1, 7))]
        yield u' '.join(paragraph)
