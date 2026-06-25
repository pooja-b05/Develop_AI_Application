from setuptools import setup, find_packages

setup(
    name="emotion_detector",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "requests"
    ]
)