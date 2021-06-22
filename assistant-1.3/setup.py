from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='assistant',
    version='1.3',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    packages=['assistant'],
    entry_points={
        'console_scripts':
            ['bot = assistant.core:start_bot']
        },
    )
