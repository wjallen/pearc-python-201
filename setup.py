from setuptools import setup, find_packages

setup(
    name='python201',
    version='0.0.1',
    license='MIT License',
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ],
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['cumprod=python201.algorithms:main']
    }
)
