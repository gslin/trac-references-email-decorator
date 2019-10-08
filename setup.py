import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TracReferencesEmailDecorator",
    version="0.20191009.0",
    author="Gea-Suan Lin",
    author_email="darkkiller@gmail.com",
    description="Add header's Message-ID field to References field for Trac.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gslin/trac-references-email-decorator",
    packages=setuptools.find_packages(),
    install_requires=["Trac>=1.1.3"],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Apprived :: MIT License",
        "Operating System :: OS :: Independent",
    ],
    python_requires=">=2.7",
    entry_points={
        "trac.plugins": "TracReferencesEmailDecorator = TracReferencesEmailDecorator"
    },
)
