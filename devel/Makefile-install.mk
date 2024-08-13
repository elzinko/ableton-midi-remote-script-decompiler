# Use zsh or bash shell explicitly
SHELL := /bin/zsh

# Variables
VENV_DIR := venv
BUNDLE_DIR := bundle
BUILD_DIR := build
DIST_DIR := dist
DOCS_DIR := docs
APP_NAME := abletoolkit
PYTHON_VERSION := 3.12.1
PYENV_ROOT := $(HOME)/.pyenv
PYTHON := $(PYENV_ROOT)/versions/$(PYTHON_VERSION)/bin/python

# clean everything, including venv and build artifacts
clean:
	@echo "Cleaning up..."
	@rm -rf $(VENV_DIR)
	@rm -rf $(BUNDLE_DIR)
	@rm -rf $(BUILD_DIR)
	@rm -rf $(DIST_DIR)
	@echo "Cleaned up."

# Check if pyenv is installed
install_pyenv:
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
setup-pyenv: install_pyenv
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
setup-venv: setup-pyenv
	@echo "Creating a virtual environment in $(VENV_DIR)..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"

# Setup pre-commit hooks
setup-pre-commit:
	@echo "Setting up pre-commit hooks..."
	pre-commit install --hook-type commit-msg --hook-type pre-push
	@echo "Pre-commit hooks set up"

# Install dependencies, abletoolkit, and setup pre-commit hooks
install: setup-venv setup-pre-commit
	@echo "Installing dependencies and Abletoolkit..."
	@mkdir -p $(BUILD_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt .
	@echo "Dependencies and Abletoolkit installed"
