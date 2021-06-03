import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OpenCEP",
    version="0.0.1",
    #author="Example Author",
    # author_email="author@example.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        # "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        # "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'autopep8',
    ],
    extras_require={
        'test': [
            'pytest',
            "tweepy",
        ],
    }
)
