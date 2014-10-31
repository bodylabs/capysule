version = '0.5.1'

# https://coderwall.com/p/qawuyq
# Thanks James.

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = ''

with open('requirements.txt', 'r') as f:
    install_requires = [x.strip() for x in f.readlines()]

from setuptools import setup, find_packages

setup(
    name='capysule',
    version=version,
    author='Body Labs',
    author_email='paul.melnikow@bodylabs.com',
    description='Bindings for Capsule CRM based on Requests and Booby',
    long_description=long_description,
    url='https://github.com/bodylabs/capysule',
    license='Apache 2',
    packages=find_packages(exclude=['*.tests', '*.tests.*' 'tests.*', 'tests']),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
