from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()
setup(
    name="xssscant3r",
    version="0.4",
    description="Web Application Security Scanner",
    long_description=long_description,
    author="DesTroTN",
    author_email="destrotn@yahoo.com",
    url="https://github.com/DesTroTN",
    packages=find_packages(),
    include_package_data=True,
    scripts=('xssscant3r',),
    entry_points={},
    install_requires=[
        "requests",
    ],
    extras_require={
        "tests": [
            "pytest",
            "pytest-forked",
            "pytest-xdist",
            "flake8",
        ],
    },
    classifiers=[
        "Operating System :: POSIX",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Security",
        "Topic :: System :: Web",
        "Topic :: Utilities",
    ],
)
