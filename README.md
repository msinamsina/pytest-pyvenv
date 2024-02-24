# Pytest-env

This is a simple plugin for pytest that allows you to set environment
variables for your tests.

## Installation

### From PyPI

```bash
pip install pytest-pyvenv
```

### From Source

```bash
pip install git+https://github.com/msinamsina/pytest-pyvenv.git
```


## Usage

```python

def test_env(pyvenv):
    pyvenv.install_package('pytest-pyvenv')
    pyvenv.run('mkdir -p tests')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue 
first to discuss what you would like to change.