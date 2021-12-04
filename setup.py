import os

from setuptools import find_packages, setup


def get_requirement(f):
    return open(os.path.join("requirements", f)).read().splitlines()


setup(
    name="human-face-recognition-app",
    version="0.0.0",
    author="Swadesh Ranjan Dash",
    description="Live Face ditecion using opencv",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=get_requirement("app.txt"),
)
