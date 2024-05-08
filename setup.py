from setuptools import setup, find_packages

setup(
    name='size_folders_package',
    version='1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'size_folders = size_folders_package.__main__:main'
        ]
    },
)
