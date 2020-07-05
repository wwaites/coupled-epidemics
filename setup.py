#!/usr/bin/env python

from setuptools import setup, find_packages

long_description = """
Some examples of Coupled Epidemics
"""

setup(name='coupled-epidemics',
      version='0.1',
      description='Coupled epidemics',
      long_description=long_description,
      url='https://github.com/wwaites/coupled-epidemics',
      author=['William Waites'],
      author_email='wwaites@inf.ed.ac.uk',
      keywords=['epidemiology', 'ecology', 'rule-based models', 'kappa'],
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 4 - Beta',

          # Intended audience
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',

          # Topics
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Life',

          # License
          'License :: OSI Approved :: GNU General Public License (GPL)',
          # Specify the Python versions you support here. In particular,
          # ensure that you indicate whether you support Python 2, Python 3
          # or both.
        'Programming Language :: Python :: 3',
      ],
      license='GPLv3',
      packages=find_packages(),
      install_requires=[
          'pandas',
      ],
      python_requires='>=3.1.*',
      package_data={
          ".": ["Makefile"],
          "models": ["*.pka"],
          "data":   ["Makefile"],
      }
)
