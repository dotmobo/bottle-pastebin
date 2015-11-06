# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = 'bottle-pastebin',
    version = '1.0.0',
    packages=find_packages(),
    include_package_data=True,
    author = 'mobo',
    author_email = 'pastebinbottle@gmail.com',
    url = 'https://github.com/dotmobo/bottle-pastebin',
    
    install_requires  = [
        'PyYAML==3.10',
        'bottle==0.11.6',
        'peewee==2.1.2',
        'psycopg2==2.5',
        'pycrypto==2.6'
    ],
    
)
