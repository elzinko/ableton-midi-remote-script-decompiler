# Variables
VENV_DIR := venv
BUILD_DIR := build
BUNDLE_DIR := bundle
PYTHON_VERSION := 3.12.1
PYENV_ROOT := $(HOME)/.pyenv
PYTHON := $(PYENV_ROOT)/versions/$(PYTHON_VERSION)/bin/python

# Clean up
clean:
	@echo "Cleaning up..."
	@rm -rf $(VENV_DIR)
	@rm -rf $(BUILD_DIR)
	@rm -rf $(BUNDLE_DIR)
	@echo "Cleaned up."

# Clean up .pyenv for tests
clean-pyenv:
	@echo "Cleaning up .pyenv..."
	@rm -rf $(PYENV_ROOT)

# Get the Python version
python-version:
	@echo $(PYTHON_VERSION)

# Install pyenv if it's not already installed
install-pyenv:
	@echo "Checking if pyenv is installed..."
	@if [ ! -d "$(PYENV_ROOT)" ]; then \
		echo "pyenv not found. Installing pyenv..."; \
		curl https://pyenv.run | bash; \
		echo "pyenv installed. Please add the following to your shell configuration:"; \
		echo 'export PATH="$(PYENV_ROOT)/bin:$$PATH"'; \
		echo 'eval "$$($(PYENV_ROOT)/bin/pyenv init --path)"'; \
		echo 'eval "$$($(PYENV_ROOT)/bin/pyenv init -)"'; \
		echo 'eval "$$($(PYENV_ROOT)/bin/pyenv virtualenv-init -)"'; \
	else \
		echo "pyenv is already installed."; \
	fi

# Ensure pyenv is set up correctly and the Python version is installed
setup-pyenv: install-pyenv
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
create-venv: setup-pyenv
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Creating a virtual environment in $(VENV_DIR)..."; \
		$(PYTHON) -m venv $(VENV_DIR); \
		echo "Virtual environment created in $(VENV_DIR)"; \
	else \
		echo "Virtual environment already exists in $(VENV_DIR)."; \
	fi

# Install dependencies and Abletoolkit (without pre-commit hooks)
install: create-venv
	@mkdir -p $(BUILD_DIR)
	@echo "Installing dependencies..."
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt
	@echo "Dependencies installed"
	$(VENV_DIR)/bin/pip install .
	@echo "Abletoolkit installed"
