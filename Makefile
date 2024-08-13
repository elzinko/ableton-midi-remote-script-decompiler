include devel/Makefile-tag.mk
include devel/Makefile-bump.mk
include devel/Makefile-bundle.mk

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


# Default target
.DEFAULT_GOAL := install

# Clean everything, including venv and build artifacts
clean:
	rm -rf $(BUILD_DIR) $(DIST_DIR) $(BUNDLE_DIR) $(DOCS_DIR)
	rm -rf $(VENV_DIR)
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type f -name '*.egg-info' -delete
	@echo "Cleaned up all generated files."


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

# Setup pre-commit hooks
setup_pre_commit:
	@echo "Setting up pre-commit hooks..."
	pre-commit install --hook-type commit-msg --hook-type pre-push

# Install dependencies, abletoolkit, and setup pre-commit hooks
install: $(VENV_DIR)/bin/activate setup_pre_commit
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt
	@echo "Dependencies installed"
	$(VENV_DIR)/bin/pip install .
	@echo "Abletoolkit installed"
	@echo "Pre-commit hooks set up"

# Run tests
test: $(VENV_DIR)/bin/activate
	$(VENV_DIR)/bin/python -m unittest discover -v
	@echo "Tests run successfully"

# Lint the code
lint: $(VENV_DIR)/bin/activate
	$(VENV_DIR)/bin/pylint $(shell find abletoolkit -name "*.py") $(shell find tests -name "*.py")
	@echo "Linting completed"

# Show the current version of abletoolkit
version:
	@python -c "from src.abletoolkit.version import __version__; print(__version__)"

# Show help
help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  clean: Clean everything, including venv and build artifacts"
	@echo "  install: Install dependencies and abletoolkit"
	@echo "  test: Run tests"
	@echo "  lint: Lint the code"
	@echo "  version: Show the current version of abletoolkit"
# Makefile-tag.mk
	@echo	"  ===== TAGS ====="
	@echo	"  fetch-tags: Fetch tags from the remote repository"
	@echo	"  push-tag: Push tags to the remote repository"
# Makefile-bump.mk
	@echo	"  ===== BUMP ====="
	@echo	"  bump-version-minor: Bump the minor version"
	@echo	"  bump-version-major: Bump the major version"
	@echo	"  bump-version-patch: Bump the patch version"
	@echo	"  bump-specific-version: Bump a specific version"
# add Makefile-bundle.mk
	@echo	"  ===== BUNDLE ====="
	@echo	"  setup-bundle: Create a virtual environment and install dependencies"
	@echo	"  bundle-release: Bundle release step: create executable and prepare docs"
	@echo	"  generate-docs: Generate documentation in markdown format"
	@echo	"  package-bundle: Package everything into a zip file"

.PHONY: clean install test lint setup_pyenv version help
		fetch-tags push-tag
		bump-version-minor
		bump-version-major
		bump-version-patch
		bump-specific-version
		setup-bundle
		bundle-release
		generate-docs
		package-bundle
