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
install-pyenv:
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
setup-pyenv:
	@echo "Checking if pyenv is installed..."
	@if ! command -v pyenv >/dev/null 2>&1; then \
		echo "pyenv not found. Installing pyenv..."; \
		curl https://pyenv.run | bash; \
		export PATH="$$HOME/.pyenv/bin:$$PATH"; \
		export PYENV_ROOT="$$HOME/.pyenv"; \
		"$$HOME/.pyenv/bin/pyenv" init --path; \
		"$$HOME/.pyenv/bin/pyenv" init -; \
		"$$HOME/.pyenv/bin/pyenv" virtualenv-init -; \
		echo "pyenv installed and initialized."; \
	else \
		echo "pyenv is already installed."; \
	fi; \
	export PATH="$$HOME/.pyenv/bin:$$PATH"; \
	export PYENV_ROOT="$$HOME/.pyenv"; \
	if ! "$$PYENV_ROOT/bin/pyenv" versions --bare | grep -q "^$(PYTHON_VERSION)$$"; then \
		echo "Python $(PYTHON_VERSION) not found. Installing via pyenv..."; \
		"$$PYENV_ROOT/bin/pyenv" install $(PYTHON_VERSION); \
	else \
		echo "Python $(PYTHON_VERSION) is already installed via pyenv."; \
	fi; \
	"$$PYENV_ROOT/bin/pyenv" global $(PYTHON_VERSION)

# Create a virtual environment
setup-venv: setup-pyenv
	@echo "Creating a virtual environment in $(VENV_DIR)..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"

# Install dependencies, abletoolkit, and setup pre-commit hooks
install: setup-venv
	@echo "Installing dependencies and Abletoolkit..."
	@mkdir -p $(BUILD_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt .
	@echo "Dependencies and Abletoolkit installed"

# Setup pre-commit hooks
setup-pre-commit: install
	@echo "Setting up pre-commit hooks..."
	$(VENV_DIR)/bin/pre-commit install --hook-type commit-msg --hook-type pre-push
	@echo "Pre-commit hooks set up"
