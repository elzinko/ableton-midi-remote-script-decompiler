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
	@$(MAKE) -f devel/Makefile-install.mk clean

# Check if pyenv is installed and set up the environment
setup-pyenv:
	@$(MAKE) -f devel/Makefile-install.mk setup-pyenv

setup-venv:
	@$(MAKE) -f devel/Makefile-install.mk setup-venv

# Create a virtual environment and install dependencies
install: setup-pyenv
	@$(MAKE) -f devel/Makefile-install.mk install

# Run tests
test:
	@$(MAKE) -f devel/Makefile-install.mk test

# Lint the code
lint:
	@$(MAKE) -f devel/Makefile-install.mk Lint

# Show the current version of abletoolkit
version:
	@$(MAKE) -f devel/Makefile-install.mk version

# Bump the version
bump-version-minor:
	@$(MAKE) -f devel/Makefile-bump.mk bump-version-minor

bump-version-major:
	@$(MAKE) -f devel/Makefile-bump.mk bump-version-major

bump-version-patch:
	@$(MAKE) -f devel/Makefile-bump.mk bump-version-patch

bump-specific-version:
	@$(MAKE) -f devel/Makefile-bump.mk bump-specific-version

# Tag management
fetch-tags:
	@$(MAKE) -f devel/Makefile-tag.mk fetch-tags

push-tag:
	@$(MAKE) -f devel/Makefile-tag.mk push-tag

# Bundle release step: create executable and prepare docs
bundle-release:
	@$(MAKE) -f devel/Makefile-bundle.mk bundle-release

# Package everything into a zip file
package-bundle:
	@$(MAKE) -f devel/Makefile-bundle.mk package-bundle

# Show help
help:
	@echo "Usage: make [target]"
	@echo "Available targets:"
	@echo "  clean: Clean everything, including venv and build artifacts"
	@echo "  setup-pyenv: Check if pyenv is installed and set up the environment"
	@echo "  setup-venv: Create a virtual environment and install dependencies"
	@echo "  install: Install dependencies and abletoolkit"
	@echo "  test: Run tests"
	@echo "  lint: Lint the code"
	@echo "  version: Show the current version of abletoolkit"
	@echo "  ===== VERSIONNING ======"
	@echo "  bump-version-minor: Bump the minor version"
	@echo "  bump-version-major: Bump the major version"
	@echo "  bump-version-patch: Bump the patch version"
	@echo "  bump-specific-version: Bump a specific version"
	@echo "  ===== TAGS ======"
	@echo "  fetch-tags: Fetch tags from the remote repository"
	@echo "  push-tag: Push the tag to the remote repository"
	@echo "  ===== GITHUB BUNDLE ONLY ======"
	@echo "  bundle-release: Create executable and prepare docs"
	@echo "  package-bundle: Package everything into a zip file"
