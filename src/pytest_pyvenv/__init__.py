import pytest
import os
import subprocess
import tempfile
from cookiecutter.utils import rmtree
import platform


@pytest.fixture
def pyvenv():
    with VenvClass() as vv:
        yield vv


class VenvClass:
    def __init__(self):
        venv_dir = tempfile.mkdtemp(dir='.')
        print(f"Creating virtual environment in {os.path.abspath(venv_dir)}")
        subprocess.run(['python', '-m', 'venv', venv_dir])
        # return python path
        if os.path.exists(os.path.join(venv_dir, "bin")):
            python_path = os.path.join(venv_dir, "bin", "python")
        elif os.path.exists(os.path.join(venv_dir, "Scripts")):
            python_path = os.path.join(venv_dir, "Scripts", "python.exe")
        else:
            raise FileNotFoundError("Python path not found")
        print(f"Python path: {python_path}")
        self.python_path = python_path.replace(os.sep, "/")
        self.env_dir = venv_dir.replace(os.sep, "/")
        if os.name == "nt":
            # Windows
            self.activator = os.path.join(venv_dir, "Scripts", "activate.bat")
            self.activator = os.path.abspath(self.activator)
        else:
            self.activator = os.path.join(venv_dir, "bin", "activate")
            self.activator = os.path.abspath(self.activator)
            print(os.listdir(os.path.abspath(venv_dir)))
            print(os.listdir(os.path.join(venv_dir, "bin")))
            self.activator = self.activator

    def __del__(self):
        print(f"Deleting virtual environment in {self.env_dir}")
        rmtree(self.env_dir)

    def install_package(self, package: str, options: list = None):

        if options:
            return subprocess.run(
                [self.python_path, "-m", "pip", "install", *options, package])
        else:
            return subprocess.run(
                [self.python_path, "-m", "pip", "install", package])

    def run(self, popenargs):
        if platform.system() != "Windows":
            popenargs = f"source {self.activator} && {popenargs}"
            return subprocess.run(popenargs, shell=True,
                                  executable="/bin/bash", capture_output=True)
        else:
            popenargs = f"{self.activator} && {popenargs}"
        return subprocess.run(popenargs, shell=True, capture_output=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self
