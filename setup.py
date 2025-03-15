from setuptools import setup, find_packages
import os

def read_requirements():
    req_file = os.path.join(os.path.dirname(__file__), "requirements/requirements.txt")
    if os.path.exists(req_file):
        with open(req_file) as f:
            return f.read().splitlines()
    return []

setup(
    name="bikeshare_model",
    version="1.0",
    packages=find_packages(),
    install_requires=read_requirements(),
)
