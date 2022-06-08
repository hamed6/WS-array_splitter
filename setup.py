from setuptools import find_packages, setup

setup(
    name='Library',
    packages=find_packages(include=['Library']),
    install_requires=['numpy==1.19.5'],
    version='1.0',
    author='Hamed'
)