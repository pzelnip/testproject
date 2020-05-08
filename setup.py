import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pzelnip-test-package",  # Replace with your own username
    version="0.0.1",
    author="Adam Parkin",
    author_email="pzelnip@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pzelnip/testproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"hello": "hello"},
    package_data={"hello": ["*.jinja2"]},
    install_requires="Jinja2 bullet click GitPython requests".split(),
    entry_points={"console_scripts": ["hello=hello.hello:main"],},
    python_requires=">=3.6",
)
