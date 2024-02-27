import pytest

from src.pytest_pyvenv import VenvClass, run_inside_dir, inside_dir


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


def test_space_in_package_path():
    with VenvClass() as venv:
        # check mypkg is not installed
        print(venv.run("mypkg --version").stdout.decode("utf-8"))
        assert venv.run("mypkg --version").returncode != 0
        # install mypkg
        assert venv.install_package("tests/my pkg").returncode == 0
        # check pytest is installed
        assert venv.run("pip show mypkg").returncode == 0
        # check mypkg is installed
        # uninstall mypkg
        assert venv.run("pip uninstall -y mypkg").returncode == 0
        # check mypkg is not installed
        assert venv.run("mypkg --version").returncode != 0


def test_space_in_venv_path():
    run_inside_dir("mkdir 'my venv'", "./tests")
    with inside_dir("tests/my venv"):
        with VenvClass() as venv:
            print(venv.run("python --version").stderr.decode("utf-8"))
            assert venv.run("python --version").returncode == 0
            # check mypkg is not installed
            print(venv.run("pip show mypkg").stdout.decode("utf-8"))
            assert venv.run("pip show mypkg").returncode != 0
            # install mypkg
            assert venv.install_package("../my pkg").returncode == 0
            # check pytest is installed
            assert venv.run("pip show mypkg").returncode == 0
            # check mypkg is installed
            # uninstall mypkg
            assert venv.run("pip uninstall -y mypkg").returncode == 0
            # check mypkg is not installed
            assert venv.run("mypkg --version").returncode != 0
