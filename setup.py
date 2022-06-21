#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
oc like tool that works with must-gather rather than OpenShift API
"""
from setuptools import find_packages, setup

import omg

dependencies = [
    "tabulate",
    "pyyaml",
    "python-dateutil",
    "cryptography>=2.5,<=3.3.2",
    "click==7.1.2",
]

setup(
    name="o-must-gather",
    version=omg.version,
    url="https://github.com/mashetty330/o-must-gather",
    description="oc like tool that works with ODF must-gather helps fetch information about the storage-cluster",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=dependencies,
    entry_points={
        "console_scripts": [
            "tedc = omg.cli:cli",
        ],
    },
)
