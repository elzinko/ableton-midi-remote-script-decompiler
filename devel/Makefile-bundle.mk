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
clean-bundle:
	rm -rf $(BUILD_DIR) $(DIST_DIR) $(BUNDLE_DIR)
	@echo "Cleaned previous builds."

# Create a virtual environment and install dependencies
setup-bundle:
	@echo "Setting up the environment..."
	@rm -rf $(VENV_DIR)
	@$(SHELL) -c "python3 -m venv $(VENV_DIR) && source $(VENV_DIR)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"
	@echo "Environment setup completed."

# Bundle release step: create executable and prepare docs
bundle-release: clean-bundle setup-bundle
	@echo "Building standalone executable with PyInstaller..."
	$(VENV_DIR)/bin/pyinstaller --onefile --name $(APP_NAME) --distpath $(BUNDLE_DIR) --workpath $(BUILD_DIR)/work --specpath $(BUILD_DIR) src/$(APP_NAME)/cli.py
	@echo "Standalone executable created in $(BUNDLE_DIR)."
	@$(MAKE) package-bundle

# Package everything into a zip file
package-bundle:
	@echo "Packaging the bundle..."
	@mkdir -p $(DIST_DIR)
	@cp docs/$(APP_NAME)-user-guide.md $(BUNDLE_DIR)
	@cd $(BUNDLE_DIR) && zip -r ../$(DIST_DIR)/$(APP_NAME)-bundle.zip *
	@echo "Bundle created as $(APP_NAME)-bundle.zip."

.PHONY: clean-bundle setup-bundle bundle-release package-bundle
