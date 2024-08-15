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


# Install tasks

clean:
	@$(MAKE) -f devel/Makefile-install.mk clean

setup-pyenv:
	@$(MAKE) -f devel/Makefile-install.mk setup-pyenv

create-venv:
	@$(MAKE) -f devel/Makefile-install.mk create-venv

install:
	@$(MAKE) -f devel/Makefile-install.mk install

# Dev tasks

test:
	@$(MAKE) -f devel/Makefile-dev.mk test

lint:
	@$(MAKE) -f devel/Makefile-dev.mk lint

commit:
	@$(MAKE) -f devel/Makefile-dev.mk commit

version:
	@$(MAKE) -f devel/Makefile-dev.mk version

bump-version-minor:
	@$(MAKE) -f devel/Makefile-dev.mk bump-version-minor

bump-version-major:
	@$(MAKE) -f devel/Makefile-dev.mk bump-version-major

bump-version-patch:
	@$(MAKE) -f devel/Makefile-dev.mk bump-version-patch

bump-specific-version:
	@$(MAKE) -f devel/Makefile-dev.mk bump-specific-version

fetch-tags:
	@$(MAKE) -f devel/Makefile-dev.mk fetch-tags

push-tag:
	@$(MAKE) -f devel/Makefile-dev.mk push-tag

# CI tasks

bundle-release:
	@$(MAKE) -f devel/Makefile-ci.mk bundle-release

package-bundle:
	@$(MAKE) -f devel/Makefile-ci.mk package-bundle

# Show help
help:
	@echo "Usage: make [target]"
	@echo "Available targets:"
	@echo "  clean: Clean the project"
	@echo "  setup-pyenv: Setup pyenv"
	@echo "  create-venv: Setup virtual environment"
	@echo "  install: Install the project"
	@echo "  test: Run tests"
	@echo "  lint: Lint the code"
	@echo "  commit: Commitizen commit"
	@echo "  version: Show the current version of abletoolkit"
	@echo "  bump-version-minor: Bump the version to the next minor"
	@echo "  bump-version-major: Bump the version to the next major"
	@echo "  bump-version-patch: Bump the version to the next patch"
	@echo "  bump-specific-version: Bump the version to a specific version"
	@echo "  fetch-tags: Fetch tags from the remote repository"
	@echo "  push-tag: Push the tag to the remote repository"
	@echo "  bundle-release: Bundle the release"
	@echo "  package-bundle: Package the bundle"
	@echo "  help: Show this help message"
	@echo ""
	@echo "For more information, please refer to the README.md file."
	@echo ""
