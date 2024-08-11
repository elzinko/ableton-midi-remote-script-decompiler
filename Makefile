# Use zsh or bash shell explicitly
SHELL := /bin/zsh

# Variables
VENV_DIR := venv
PYTHON_VERSION := 3.12.1
PYENV_ROOT := $(HOME)/.pyenv
PYTHON := $(PYENV_ROOT)/versions/$(PYTHON_VERSION)/bin/python

# Default target
.DEFAULT_GOAL := install

# Check if pyenv is installed
$(PYENV_ROOT):
	@echo "Checking if pyenv is installed..."
	@if [ ! -d "$(PYENV_ROOT)" ]; then \
		echo "pyenv not found. Installing pyenv..."; \
		curl https://pyenv.run | zsh; \
		echo "pyenv installed. Please add the following to your shell configuration:"; \
		echo 'export PATH="$(PYENV_ROOT)/bin:$$PATH"'; \
		echo 'eval "$$($(PYENV_ROOT)/bin/pyenv init --path)"'; \
		echo 'eval "$$($(PYENV_ROOT)/bin/pyenv init -)"'; \
		echo 'eval "$$($(PYENV_ROOT)/bin/pyenv virtualenv-init -)"'; \
	else \
		echo "pyenv is already installed."; \
	fi

# Ensure pyenv is set up correctly and the Python version is installed
setup_pyenv: $(PYENV_ROOT)
	@echo "Initializing pyenv..."
	@if ! $(PYENV_ROOT)/bin/pyenv versions --bare | grep -q "^$(PYTHON_VERSION)$$"; then \
		echo "Python $(PYTHON_VERSION) not found. Installing via pyenv..."; \
		$(PYENV_ROOT)/bin/pyenv install $(PYTHON_VERSION); \
	else \
		echo "Python $(PYTHON_VERSION) is already installed via pyenv."; \
	fi
	@$(PYENV_ROOT)/bin/pyenv local $(PYTHON_VERSION)
	@echo "Python $(PYTHON_VERSION) set as local version."

# Create a virtual environment
$(VENV_DIR)/bin/activate: setup_pyenv
	@echo "Creating a virtual environment in $(VENV_DIR)..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"

# Install
install: $(VENV_DIR)/bin/activate
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt
	@echo "Dependencies installed"
	$(VENV_DIR)/bin/pip install .
	@echo "Abletoolkit installed"

# Run tests
test: $(VENV_DIR)/bin/activate
	$(VENV_DIR)/bin/python -m unittest discover -v
	@echo "Tests run successfully"

# Lint the code
lint: $(VENV_DIR)/bin/activate
	$(VENV_DIR)/bin/pylint $(shell find abletoolkit -name "*.py") $(shell find tests -name "*.py")
	@echo "Linting completed"

# Clean everything, including venv and build artifacts
clean:
	rm -rf $(VENV_DIR)
	rm -rf build dist *.egg-info
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	@echo "Cleaned up all generated files, including the venv and build artifacts."

version:
	@echo src/abletoolkit/version.py | xargs grep __version__ | cut -d '"' -f 2

.PHONY: install test lint clean setup_pyenv
