# #######################################################################################
# ---------------------------------------------------------------------------------------
# File:   setup.py
# Author: Luis Monteiro
# ---------------------------------------------------------------------------------------
# #######################################################################################
# imports
from setuptools import setup, find_packages
# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------
with open('readme.md', 'r') as fh:
    long_description = fh.read()
# -----------------------------------------------------------------------------
# setup
# -----------------------------------------------------------------------------
setup(
    name='smelter',  
    version='0.1',
    author='Luis Monteiro',
    author_email='monteiro.lcm@gmail.com',
    description='Build Tool',
    long_description=long_description,
    packages=[
        'smelter',
    ],
    install_requires=[
        'cmake',
        'git'
    ],
    entry_points={
      'console_scripts': [
          'smelter = smelter.worker:main',
      ]
    }
 )
# #######################################################################################
# ---------------------------------------------------------------------------------------
# End
# ---------------------------------------------------------------------------------------
# #######################################################################################
