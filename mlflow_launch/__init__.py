# mlflow_launch/__init__.py

"""
MLflow Server Launcher Package

This package provides a convenient way to start the MLflow tracking server
from a Python script or Jupyter Notebook.
"""
import os
import pathlib


def _load_version():
    root = pathlib.Path(__file__).resolve().parent.parent
    version_file = root / "_version.py"
    ns = {}
    with open(version_file) as f:
        exec(f.read(), ns)
    return ns["__version__"]


__author__ = """Jason Conner"""
__email__ = "jason.conner@noaa.gov"
__version__ = _load_version()

from .launcher import start_mlflow_server
