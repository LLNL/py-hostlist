import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-hostlist",
    version="0.0.1-dev",
    author="Christopher Moussa",
    author_email="moussa1@llnl.gov",
    description="A slurm-style hostlist processor.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/example-project",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'hostlist = hostlist.cla_hostlist:main',
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
