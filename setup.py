import os
from setuptools import setup


setup(
    name='flask-mplayer',
    version='1.0',
    description='Music player with flask',
    author='Sebastian Robert Karlsson',
    author_email='sebbekarlsson97@gmail.com',
    url='http://www.ianertson.com/',
    install_requires=[
        'flask',
        'flask-wtf',
        'PyMySQL',
        'pygame',
        'mplayer.py',
        'sqlalchemy'
    ]
)