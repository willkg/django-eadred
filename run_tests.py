#!/usr/bin/env python

import os
import sys

import nose


# Set up the environment for our test project.
ROOT = os.path.abspath(os.path.dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'
sys.path.insert(0, os.path.join(ROOT, 'examples'))

# This can't be imported until after we've fiddled with the
# environment.
from django.test.utils import setup_test_environment
setup_test_environment()

# Run nose.
#
# nose.run() returns True if tests passed and False otherwise which is
# the inverse of what we want the process to return, so we invert it.
sys.exit(not nose.run())
