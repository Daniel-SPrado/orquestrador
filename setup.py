from setuptools import setup, find_packages

setup(
    name='dims',
    version=version,
    description='DIMS is a module of the UIoT middleware.',
    url='https://uiot.org/',
    long_description=long_description,
    author='Dayanne Fernandes, Lucas Martins, Thiago Araújo',
    author_email='danielsprado12@gmail.com'
    packages=find_packages(exclude='tests'),
    install_requires=['time', 'requests', 'json']
)
