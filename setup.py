from setuptools import setup, find_packages

setup(
    name = 'songcalc',
    version = '0.1.0',
    packages = ['songcalc'],
    install_requires=['Click'],
    entry_points = {
        'console_scripts': [
            'songcalc = songcalc.__main__:main'
        ]
    })
