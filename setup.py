import os
from setuptools import setup


def read_relative_file(filename):
    """Returns contents of the given file, which path is supposed relative
    to this module."""
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read().strip()


NAME = 'django-generic-filters'
README = read_relative_file('README.rst')
VERSION = read_relative_file('VERSION')
PACKAGES = ['django_genericfilters']
REQUIRES = [
    'Django',
    'munch',
]


if __name__ == '__main__':  # Don't run setup() when we import this module.
    setup(name=NAME,
          version=VERSION,
          description='Easy filters for your Generic ListView with Django.',
          long_description=README,
          classifiers=['Development Status :: 4 - Beta',
                       'License :: OSI Approved :: BSD License',
                       'Programming Language :: Python :: 3',
                       'Programming Language :: Python :: 3.6',
                       'Programming Language :: Python :: 3.7',
                       'Programming Language :: Python :: 3.8',
                       'Framework :: Django',
                       ],
          keywords='class-based view, generic view, filters',
          author='Novapost Team',
          author_email='peopleask@novapost.fr',
          url='https://github.com/novapost/%s' % NAME,
          license='BSD',
          packages=PACKAGES,
          include_package_data=True,
          install_requires=REQUIRES,
          setup_requires=['setuptools'],
          )
