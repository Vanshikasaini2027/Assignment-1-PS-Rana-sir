from setuptools import setup, find_packages

setup(
    name="Topsis-Vanshika-102303735",
    version="0.1",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
    author="Vanshika Saini",
    description="TOPSIS implementation using Python",
)
