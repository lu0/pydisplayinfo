#!/usr/bin/env python3

import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

CURRENT_PY_VERSION = sys.version_info[:2]
REQUIRED_PY_VERSION = (3, 7)

if CURRENT_PY_VERSION < REQUIRED_PY_VERSION:
    sys.stderr.write(
        """
pydisplayinfo requires at least Python {}.{},
but Python {}.{} was detected. Please upgrade.
        """.format(
            *REQUIRED_PY_VERSION, *CURRENT_PY_VERSION
        )
    )
    sys.exit(1)


class Test(TestCommand):
    user_options = [("pytest-args=", "a", "Options for pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        # Empty since this is a fallback for `pytest tests`,
        # which uses the options adopted in the `.toml` file.
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        error = pytest.main(self.pytest_args)
        sys.exit(error)


install_requires = []

package_info = dict()
current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, "pydisplayinfo", "__version__.py")) as f:
    exec(f.read(), package_info)

readme = ""
with open("README.md") as f:
    readme = f.read()

setup(
    name=package_info["__package_name__"],
    version=package_info["__version__"],
    description=package_info["__description__"],
    long_description=readme,
    author=package_info["__author__"],
    author_email=package_info["__author_email__"],
    url=package_info["__url__"],
    long_description_content_type="text/markdown",
    packages=["pydisplayinfo"],
    package_data={"": ["LICENSE"]},
    package_dir={"pydisplayinfo": "pydisplayinfo"},
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Multimedia :: Video :: Display",
        "Topic :: Software Development :: Libraries",
        "Topic :: Desktop Environment :: Window Managers",
    ],
    cmdclass={"test": Test},
    project_urls={
        "Source Code": package_info["__url__"],
        "E-mail": package_info["__author_email__"],
    },
)
