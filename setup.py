from setuptools import setup, find_packages

setup(
    name="cryptobots2025",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List your package dependencies here
    ],
)