from pathlib import Path

from setuptools import find_packages, setup

CURRENT_DIR = Path(__file__).parent


def get_long_description() -> str:
    return (CURRENT_DIR / "README.md").read_text(encoding="utf8")


setup(
    name="docker-charon",
    version="0.1.0",
    description="A tool to move your Docker images to an air-gapped registry.",
    install_requires=(CURRENT_DIR / "requirements.txt").read_text().splitlines(),
    packages=find_packages(),
    include_package_data=True,  # will read the MANIFEST.in
    license="MIT",
    python_requires=">=3.7, <4",
)