# mlflow_launch/__init__.py

"""
MLflow Server Launcher Package

This package provides a convenient way to start the MLflow tracking server
from a Python script or Jupyter Notebook.
"""
import os
import pathlib

__author__ = """Jason Conner"""
__email__ = "jason.conner@noaa.gov"
__version__ = "1.0.7"

from .launcher import start_mlflow_server
