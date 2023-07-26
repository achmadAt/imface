from setuptools import setup

dependecies = ['deepface']

setup(
    name='lspy',
    version='0.1',
    install_requires=dependecies,
    entry_points={"console_scripts": ["imface=imface.main:main"]},
    author="Achmad Alfazari",
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Programming Language :: Python",
    ],
)