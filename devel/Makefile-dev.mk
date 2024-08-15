# Variables
VENV_DIR := venv

# Setup pre-commit hooks (development-only)
setup-pre-commit:
	@if [ ! -d "$(VENV_DIR)" ] || [ ! -f "$(VENV_DIR)/bin/activate" ]; then \
		echo "Virtual environment is not properly set up. Please run 'make install-dev' or 'make install' first."; \
		exit 1; \
	fi
	@echo "Setting up pre-commit hooks..."
	pre-commit install --hook-type commit-msg --hook-type pre-push

# Install and add pre-commit
install-dev:
	@$(MAKE) -f devel/Makefile-install.mk install
	@$(MAKE) -f devel/Makefile-dev.mk setup-pre-commit

# Run tests
test:
	@if [ ! -d "$(VENV_DIR)" ] || [ ! -f "$(VENV_DIR)/bin/activate" ]; then \
		echo "Virtual environment is not properly set up. Please run 'make install' first."; \
		exit 1; \
	fi
	$(VENV_DIR)/bin/python -m unittest discover -v
	@echo "Tests run successfully"

# Lint the code
lint:
	@if [ ! -d "$(VENV_DIR)" ] || [ ! -f "$(VENV_DIR)/bin/activate" ]; then \
		echo "Virtual environment is not properly set up. Please run 'make install' first."; \
		exit 1; \
	fi
	$(VENV_DIR)/bin/pylint $(shell find abletoolkit -name "*.py") $(shell find tests -name "*.py")
	@echo "Linting completed"

# Show the current version of abletoolkit
version:
	@if [ ! -d "$(VENV_DIR)" ] || [ ! -f "$(VENV_DIR)/bin/activate" ]; then \
		echo "Virtual environment is not properly set up. Please run 'make install' first."; \
		exit 1; \
	fi
	@python -c "from src.abletoolkit.version import __version__; print(__version__)"

# Commitizen commit
commit:
	@git-cz

# Fetch tags from the remote repository
fetch-tags:
	git fetch --tags

# Push the tag to the remote repository
push-tag: fetch-tags
	git push --follow-tags origin master

bump-version-minor:
	cz bump --increment MINOR

bump-version-major:
	cz bump --increment MAJOR

bump-version-patch:
	cz bump --increment PATCH
