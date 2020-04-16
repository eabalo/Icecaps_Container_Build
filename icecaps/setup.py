from setuptools import setup

setup (
    name='icecaps',
    version='0.2.0',
    packages=['icecaps',
        'icecaps.data_io',
        'icecaps.util',
        'icecaps.decoding',
        'icecaps.estimators'
    ]
)