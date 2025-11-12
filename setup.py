from setuptools import setup, find_packages

setup(
    name='cochdnn',
    version='0.1',
    packages=find_packages(),  # Automatically finds all packages in the directory
    include_package_data=True,  # Include package data specified in MANIFEST.in
    package_data={
        '': ['*.cpp', '*.cu'],  # Include all .cpp files in the package
    },
)