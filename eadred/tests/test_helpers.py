import unittest

from eadred import helpers


class TestHelpers(unittest.TestCase):
    def setUp(self):
        helpers.reset_counter()

    def test_make_unique(self):
        gen = helpers.make_unique(helpers.name_generator())
        assert gen.next().endswith('0')
        assert gen.next().endswith('1')
        assert gen.next().endswith('2')
    
    def test_name_generator(self):
        gen = helpers.name_generator()
        assert gen.next() in helpers.ENGLISH_MONARCHS

        names = ['alice', 'bob', 'harry']
        gen = helpers.name_generator(names=names)
        assert gen.next() in names

    def test_email_generator(self):
        gen = helpers.email_generator()
        email = gen.next()
        assert '@' in email
        name, domain = email.split('@')
        assert domain in helpers.DOMAINS

        names = ['alice']
        domains = ['test.example.com']
        gen = helpers.email_generator(names=names, domains=domains)
        email = gen.next()
        assert '@' in email
        name, domain = email.split('@')
        assert name in names
        assert domain in domains

        names = ['alice']
        domains = ['test.example.com']
        gen = helpers.email_generator(names=names, domains=domains,
                                      unique=True)
        email = gen.next()
        assert '@' in email
        name, domain = email.split('@')
        assert name.endswith('0')
        assert domain in domains

    def test_sentence_generator(self):
        gen = helpers.sentence_generator()
        assert gen.next() in helpers.LOREM

        sentences = ['gah!', 'oh noes!', 'phooey!']
        gen = helpers.sentence_generator(sentences=sentences)
        assert gen.next() in sentences

    def test_paragraph_generator(self):
        # These are a bit goofy since we're dealing with paragraph
        # generation and paragraphs are potentially big. Mostly we
        # want to verify it doesn't error out and that it's returning
        # something.
        gen = helpers.paragraph_generator()
        gen.next()

        sentences = ['gah!']
        gen = helpers.paragraph_generator(sentences=sentences)
        paragraph = gen.next()
        assert sentences[0] in paragraph
