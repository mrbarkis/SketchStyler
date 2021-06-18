try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os import path


config = {
    "description": "Styles hand-drawn rgb sketches.",
    "author": "Mr. Barkis",
    "url": "URL to get it at.",
    "download_url": "Where to download it",
    "author_email": "mister.barkis@gmail.com",
    "version": "0.1dev",
    "install_requires": [
        "pytest",
        "numpy",
        "matplotlib",
        "scikit-image",
        "opencv-python",
    ],
    "package_data": {
        "sketchstyler": [
            path.join(".", "img", "*"),
            path.join(".", "palettes", "palettes.json"),
        ]
    },
    "include_package_data": True,
    "packages": ["sketchstyler"],
    "scripts": [path.join(".", "bin", "rgb2.py")],
    "name": "sketchstyler",
}

setup(**config)
