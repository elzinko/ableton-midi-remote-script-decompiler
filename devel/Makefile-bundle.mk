# Variables
APP_NAME := abletoolkit
VENV_DIR := venv
BUILD_DIR := build
DIST_DIR := dist
BUNDLE_DIR := bundle
DOCS_DIR := docs

# Default target
.DEFAULT_GOAL := bundle-release

# Bundle release step: create executable and prepare docs
bundle-release:
	if [ ! -d "$(VENV_DIR)" ] || [ ! -f "$(VENV_DIR)/bin/activate" ]; then \
		echo "Virtual environment is not properly set up. Please run 'make install' first."; \
		exit 1; \
	fi
	@echo "Building standalone executable with PyInstaller..."
	@mkdir -p $(BUNDLE_DIR)
	$(VENV_DIR)/bin/pyinstaller --onefile --name $(APP_NAME) --distpath $(BUNDLE_DIR) --workpath $(BUNDLE_DIR)/work --specpath $(BUILD_DIR) src/$(APP_NAME)/cli.py
	@echo "Standalone executable created in $(BUNDLE_DIR)."
	@$(MAKE) package-bundle

# Package everything into a zip file
package-bundle:
	@echo "Packaging the bundle..."
	@cp $(DOCS_DIR)/$(APP_NAME)-user-guide.md $(BUNDLE_DIR)
	@zip -j -r $(BUNDLE_DIR)/$(APP_NAME)-bundle.zip $(BUNDLE_DIR)/$(APP_NAME) $(APP_NAME)-user-guide.md
	@echo "Bundle created as $(APP_NAME)-bundle.zip in $(BUNDLE_DIR)."

.PHONY: bundle-release package-bundle
