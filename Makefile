# Makefile for the 'easy use'
.PHONY: clean install


install:
	@echo "Installing..."
	pip install -e .[all]

uninstall:
	@echo "Uninstalling..."
	pip uninstall -y pytest-env

clean:
	@echo "Cleaning..."
	- rm -rf build dist *.egg-info
	- rm -rf .pytest_cache .coverage htmlcov
	- rm -rf */__pycache__
	- rm -rf */.pytest_cache
	- rm -rf */.coverage
	- rm -rf */*.egg-info
	- rm -rf ./*.pyc


test: clean
	@echo "Testing..."
	pytest -v

coverage: clean
	@echo "Testing with coverage..."
	- coverage run -m pytest tests -v
	@echo "Coverage report..."
	- coverage report -m

slow_coverage: clean
	@echo "Testing with coverage..."
	- coverage run -m pytest tests -v -m "slow"
	@echo "Coverage report..."
	- coverage report -m

fast_coverage: clean
	@echo "Testing with coverage..."
	- coverage run -m pytest tests -v -m "not slow"
	@echo "Coverage report..."
	- coverage report -m

lint:
	@echo "Linting..."
	- flake8 .
