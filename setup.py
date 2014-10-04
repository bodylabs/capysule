version = '0.4'

# https://coderwall.com/p/qawuyq
# Thanks James.

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = ''

# with open('requirements.txt', 'r') as f:
#     install_requires = [x.strip() for x in f.readlines()]
# Need to sort out how to distribute the Booby fork
install_requires = ['requests']

from setuptools import setup

setup(
    name='capysule',
    version=version,
    author='Body Labs',
    author_email='paul.melnikow@bodylabs.com',
    description='Bindings for Capsule CRM based on Requests and Booby',
    long_description=long_description,
    url='https://github.com/bodylabs/capysule',
    license='Apache 2',
    packages=[
        'capysule',
    ],
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
