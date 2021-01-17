from setuptools import setup, find_packages

setup(
    name='elopy',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/Petesuchos/elo-calculator',
    license='MIT',
    author='Thelmo Martins',
    author_email='thelmo@gmail.com',
    description='A simple ELO rating calculator',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        elo=elopy.scripts.cli:cli
    ''',
)
