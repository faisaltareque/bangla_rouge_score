# import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

# setuptools.setup(
#     name="rouge_score",
#     author="Google LLC",
#     author_email="no-reply@google.com",
#     description="Pure python implementation of ROUGE-1.5.5.",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     packages=['rouge_score'],
#     package_dir = {'rouge_score':''},
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: Apache Software License"
#     ],
#     install_requires=[
#         "absl-py",
#         "nltk",
#         "numpy",
#         "six>=1.14.0",
#     ],
#     python_requires='>=3.6',
# )

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bangla_rouge_score",
    description="Pure python implementation of ROUGE-1.5.5.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=[
        "TurkishStemmer @ git+https://github.com/otuncelli/turkish-stemmer-python@0c22380bf84a5ab1f219f4a905274c78afa04ed1",
        "absl-py",
        "bengali-stemmer @ git+https://github.com/abhik1505040/bengali-stemmer@375186caee8e50e3260dd6bc02d20d50277f3e39",
        "nltk",
        "numpy",
        "pythainlp==3.0.8",
        "pyonmttok==1.37.1",
        "six>=1.14.0",
        "fugashi==1.2.1",
        "jieba==0.42.1",
    ],
    python_requires='>=3.6',
)
