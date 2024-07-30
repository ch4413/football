from distutils.core import setup
from setuptools import find_packages


setup(name='mypackage',
      version='0.1',
      description='My Package',
      author='Chris Hughes',
      author_email='chris.hughes@newtoneurope.com',
      include_package_data=True,
      package_data={'': ['data/*.csv']},
      url='https://www.python.org',
      packages=find_packages()
      )
