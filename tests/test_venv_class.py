import pytest

from src.pytest_env import VenvClass


def test_install_package():
    with VenvClass() as venv:
        # check mypkg is not installed
        print(venv.run("mypkg --version").stdout.decode("utf-8"))
        assert venv.run("mypkg --version").returncode != 0
        # install mypkg
        assert venv.install_package("tests/mypkg").returncode == 0
        # check pytest is installed
        assert venv.run("pip show mypkg").returncode == 0


def test_fixture_install_package(pyvenv):
    # check mypkg is not installed
    print(pyvenv.run("mypkg --version").stdout.decode("utf-8"))
    assert pyvenv.run("mypkg --version").returncode != 0
    # install mypkg
    assert pyvenv.install_package("tests/mypkg").returncode == 0
    # check pytest is installed
    assert pyvenv.run("pip show mypkg").returncode == 0


@pytest.mark.slow
def test_install_package_with_options():
    with VenvClass() as venv:
        # check mypkg is not installed
        print(venv.run("mypkg --version").stdout.decode("utf-8"))
        assert venv.run("mypkg --version").returncode != 0
        # install mypkg
        assert venv.install_package("tests/mypkg",
                                    ["--no-deps"]).returncode == 0
        # check pytest is installed
        assert venv.run("pip show mypkg").returncode == 0
