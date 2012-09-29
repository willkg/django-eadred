import imp
import unittest

from django.test.utils import override_settings
from django.utils.importlib import import_module

from nose.tools import eq_

from eadred.management.commands import generatedata


class TestGenerateData(unittest.TestCase):
    def reset_app_data(self):
        from django.conf import settings
        for app in settings.INSTALLED_APPS:
            try:
                app_path = import_module(app).__path__
            except AttributeError:
                continue

            try:
                imp.find_module('sampledata', app_path)
            except ImportError:
                continue

            module = import_module('%s.sampledata' % app)
            module.reset_app()

    def setUp(self):
        self.reset_app_data()

    @override_settings(INSTALLED_APPS=['testproject.testapp'])
    def test_generatedata(self):
        """Test to make sure function gets called."""
        from testproject.testapp import sampledata

        cmd = generatedata.Command()
        cmd.run_from_argv(['manage.py', 'generatedata'])
        eq_(sampledata.called, True)

    @override_settings(INSTALLED_APPS=['testproject.testapp2'])
    def test_generatedata_params(self):
        """Test options passing."""
        from testproject.testapp2 import sampledata

        cmd = generatedata.Command()
        cmd.run_from_argv(
            ['manage.py', 'generatedata', '--with=dataset=random'])
        eq_(sampledata.called_with_param, 'random')

        self.reset_app_data()

        cmd.run_from_argv(
            ['manage.py', 'generatedata', '--with=dataset=basic'])
        eq_(sampledata.called_with_param, 'basic')

    @override_settings(
        INSTALLED_APPS=[
            'testproject.testapp',
            'testproject.testapp2'])
    def test_generatedata_specified_apps(self):
        """Test app specification."""
        from testproject.testapp import sampledata as testapp_sampledata
        from testproject.testapp2 import sampledata as testapp2_sampledata

        cmd = generatedata.Command()
        cmd.run_from_argv(['manage.py', 'generatedata', 'testproject.testapp'])
        eq_(testapp_sampledata.called, True)
        eq_(testapp2_sampledata.called_with_param, testapp2_sampledata.DEFAULT)
