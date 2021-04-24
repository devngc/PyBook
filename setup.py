import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="pybook",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author="Devang",
    author_email="devang@outlook.in",
    description="To learn Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devngc/pybook",
    packages=setuptools.find_packages(exclude=["tests*"]),
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        "console_scripts": ["pybook = pybook.cli:main"]
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent"
    ],
    license="AGPL-3.0"
)
