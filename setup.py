from distutils.core import setup
from setuptools import find_packages


setup(name='footballanalysis',
      version='0.1',
      description='My Package',
      author='Chris Hughes',
      author_email='chris.hughes@bath.edu',
      include_package_data=True,
      package_data={'': ['data/*.csv']},
      url='https://www.python.org',
      packages=find_packages()
      )
