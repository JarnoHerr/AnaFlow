#!/usr/bin/env python
"""
AnaFlow

python libary containing analytical and semi-analytical solutions
for pumping-test:
    thiem - steady-state, confiend- and homogeneous aquifer
    theis - transient-state, confiend- and homogeneous aquifer
    ext_thiem2D - steady-state, confiend- and heterogeneous aquifer in 2D
    ext_thiem3D - steady-state, confiend- and heterogeneous aquifer in 3D
    ext_theis2D - transient-state, confiend- and heterogeneous aquifer in 2D
    ext_theis3D - transient-state, confiend- and heterogeneous aquifer in 3D
    diskmodel - transient-state, confiend- and heterogeneous aquifer in 2D

by Sebastian Mueller 2017
"""
from setuptools import setup, find_packages

DOCLINES = __doc__.split("\n")

readme = open('LICENSE').read()

CLASSIFIERS = """\
Development Status :: 5 - alpha
Intended Audience :: Developers
Intended Audience :: End Users/Desktop
Intended Audience :: Science/Research
License :: None
Natural Language :: English
Operating System :: MacOS
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Scientific/Engineering
Topic :: Software Development
Topic :: Utilities
"""

MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


metadata = dict(
    name='anaflow',
    version=VERSION,
    maintainer="Sebastian Mueller",
    maintainer_email="sebastian.mueller (at) ufz (dot) de",
    description=DOCLINES[0],
    long_description=readme,
    author="Sebastian Mueller",
    author_email="sebastian.mueller (at) ufz (dot) de",
    license='LGPL -  see LICENSE',
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    include_package_data=True,
    install_requires=['numpy', 'scipy'],
    packages=find_packages(),
    )

setup(**metadata)