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

# Default target
.DEFAULT_GOAL := bundle-release

# Clean previous builds
clean:
	rm -rf $(BUILD_DIR) $(DIST_DIR) $(BUNDLE_DIR) $(DOCS_DIR)
	@echo "Cleaned previous builds."

# Create a virtual environment and install dependencies
setup:
	@echo "Setting up the environment..."
	@rm -rf $(VENV_DIR)
	@$(SHELL) -c "python3 -m venv $(VENV_DIR) && source $(VENV_DIR)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"
	@echo "Environment setup completed."

# Bundle release step: create executable and prepare docs
bundle-release: clean setup
	@echo "Building standalone executable with PyInstaller..."
	$(VENV_DIR)/bin/pyinstaller --onefile --name $(APP_NAME) --distpath $(BUNDLE_DIR) --workpath $(BUILD_DIR)/work --specpath $(BUILD_DIR) src/$(APP_NAME)/cli.py
	@echo "Standalone executable created in $(BUNDLE_DIR)."
	@$(MAKE) generate-docs
	@$(MAKE) package-bundle

# Generate documentation in markdown format
generate-docs:
	@echo "Generating user documentation..."
	@mkdir -p $(DOCS_DIR)
	@echo "# $(APP_NAME) Installation and Usage Guide" > $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\n## Installation" >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\nTo install $(APP_NAME), follow these steps:" >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\n1. Download the executable from the release page." >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\n2. Move the executable to a directory in your PATH." >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\n## Usage" >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\nTo use $(APP_NAME), you can run the following commands:" >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\n- `$(APP_NAME) -h`: Display help." >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\n- `$(APP_NAME) ableton -l`: List installed versions of Ableton." >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\n- `$(APP_NAME) scripts -l`: List MIDI Remote Scripts." >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\n- `$(APP_NAME) pyc -v <path_to_pyc>`: Get Python version of a .pyc file." >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\n- `$(APP_NAME) pyc -d <source_dir> <output_dir>`: Decompile .pyc files." >> $(DOCS_DIR)/$(APP_NAME)-guide.md
	@echo "\nDocumentation generated at $(DOCS_DIR)/$(APP_NAME)-guide.md."

# Package everything into a zip file
package-bundle:
	@echo "Packaging the bundle..."
	@mkdir -p $(BUNDLE_DIR)/docs
	@cp $(DOCS_DIR)/$(APP_NAME)-guide.md $(BUNDLE_DIR)/docs/
	@cd $(BUNDLE_DIR) && zip -r ../$(APP_NAME)-bundle.zip *
	@echo "Bundle created as $(APP_NAME)-bundle.zip."

.PHONY: clean setup bundle-release generate-docs package-bundle
