import os

from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ASCII Video Player',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'ascii-video-player=main:main',
        ],
    },
    # Metadata
    author='Jordan Mitacek',
    author_email='jordan.mitacek@example.com',
    description='Play videos as ASCII animations in the terminal.',
    long_description=open('README.rst').read() if os.path.exists('README.rst') else '',
    url='https://github.com/Darkkid819/asciipy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)