import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "corona_alrimi",
    version = "0.0.2",
    author = "Jiwoo Kim, Raewoo Kang, Yongchan Lee",
    author_email = "matmang@hanyang.ac.kr",
    description = "국내 코로나 현황을 알려주는 패키지",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/matmang/jaram-python-project",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "beautifulsoup4==4.9.0",
        "selenium==3.141.0",
        "requests==2.23.0"
    ]
)