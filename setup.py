import setuptools
from pathlib import Path


long_description = Path('README.md').read_text()

setuptools.setup(
    name="printc",
    version="0.0.1",
    author="Filip Wiechec",
    author_email="filip.wiechec@gmail.com",
    description="Print with colors. Eight of them.",
    entry_points = {
        "console_scripts": ["printc=printc:main"],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/filwie/printc",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: POSIX :: Linux",
                 "Operating System :: Unix",
                 "Operating System :: MacOS X",
                 "Environment :: Console",
                 ],
)
