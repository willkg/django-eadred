import os
import re
from setuptools import find_packages, setup


READMEFILE = "README.rst"
VERSIONFILE = os.path.join("eadred", "_version.py")
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"


def get_version():
    verstrline = open(VERSIONFILE, "rt").read()
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError(
            "Unable to find version string in %s." % VERSIONFILE)


setup(
    name='eadred',
    version=get_version(),
    description='Django app for generating sample data',
    long_description=open(READMEFILE).read(),
    url='https://github.com/willkg/django-eadred',
    author='Will Kahn-Greene',
    author_email='willg@bluesock.org',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
        ],
)
