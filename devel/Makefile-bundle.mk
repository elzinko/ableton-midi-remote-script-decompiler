# Variables
VENV_DIR := venv
APP_NAME := abletoolkit
BUILD_DIR := build
DOCS_DIR := docs
BUNDLE_DIR := $(BUILD_DIR)/bundle
DIST_DIR := dist

# Default target
.DEFAULT_GOAL := bundle-release

# Bundle release step: create executable and prepare docs
bundle-release:
	@echo "Building standalone executable with PyInstaller..."
	@mkdir -p $(BUNDLE_DIR)
	$(VENV_DIR)/bin/pyinstaller --onefile --name $(APP_NAME) --distpath $(BUNDLE_DIR) --workpath $(BUILD_DIR)/work --specpath $(BUILD_DIR) src/$(APP_NAME)/cli.py
	@echo "Standalone executable created in $(BUNDLE_DIR)."
	@$(MAKE) package-bundle

# Package everything into a zip file
package-bundle:
	@echo "Packaging the bundle..."
	@mkdir -p $(DIST_DIR)
	@cp $(DOCS_DIR)/$(APP_NAME)-user-guide.md $(BUNDLE_DIR)
	@zip -j -r $(DIST_DIR)/$(APP_NAME)-bundle.zip $(BUNDLE_DIR)/
	@echo "Bundle created as $(APP_NAME)-bundle.zip in $(DIST_DIR)."

.PHONY: bundle-release package-bundle
