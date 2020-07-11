import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    # Version should be updated per git push
    version="0.1.0.dev0",

    # Install requires should have required packages and updated anytime a
    # new dependency is added
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],

    # Following should change only when neccessary, ex when using new python
    # version
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
    ],
    description="",

    # Following should be updated only when installing template per README.md
    name="pysenberg",
    # author="Ashton Alexander",
    # author_email="aalexander@lighthouseglobal.com",
    # url="https://lhediscovery.visualstudio.com/DefaultCollection/Prism/_git/python_starter_template",

    # Following shouldn't need to be changed
    license='BSD-2-Clause',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False
)
