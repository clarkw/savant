from setuptools import setup

setup(
    name='songcalc',
    version='0.9.0',
    packages=['songcalc'],
    install_requires=['Click'],
    entry_points={
        'console_scripts': [
            'songcalc = songcalc.__main__:main'
        ]
    })
