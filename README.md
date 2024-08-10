# AbleToolKit

## Description
This project is a small utility for Ableton midi remote scripts developers.
Here are examples of functionnalities it provides : 
- decompile the compiled files of Ableton Live's remote scripts into another directory.
- list all Ableton Live installed versions
- list all Ableton midi remote scripts locations

## Prerequisites
- **Python 3.x** must be installed on your machine.
- **pyenv** for managing Python versions (optional but recommended).
- **pip** for installing Python packages.
- **uncompyle6** for decompiling files.

## Installation

### Step 1: Install pyenv (optional)
If you haven't installed it yet, here's how to do it:

```bash
curl https://pyenv.run | bash
```

Then, add the following lines to your `/.bashrc` or `/.zshrc` file:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Reload your shell:

```bash
source ~/.bashrc # or source ~/.zshrc
```

### Step 2: Install the correct version of Python
Use `pyenv` to install and use a specific version of Python:

```bash
pyenv install 3.x.x
pyenv global 3.x.x
```

### Step 3: Install pip
If pip is not already installed, you can install it by downloading get-pip.py and running it:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Step 4: Create a virtual environment
Create and activate a virtual environment for the project:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### Step 5: Install dependencies
Install the required dependencies with `pip`:

```bash
pip install -r requirements.txt
```

## Usage
AbleToolKit provides a command-line interface (CLI) client that allows you to access all of its functionalities easily.

To use the CLI client, simply run the following command:

```bash
abletoolkit -h
```

This will display a help message showing all available commands and options.

Example output:

```bash
usage: abletoolkit [-h] {decompile,list_versions,list_remote_scripts} ...

Decompilation and management tools for Ableton Live.

positional arguments:
  {decompile,list_versions,list_remote_scripts}
                        Command to execute
    decompile           Decompile Ableton's compiled files
    list_versions       List the installed versions of Ableton
    list_remote_scripts List MIDI Remote Scripts directories

optional arguments:
  -h, --help            show this help message and exit
```

## Available Commands

1 - Decompile Ableton Live Scripts:

To decompile Ableton Live's scripts:

```bash
abletoolkit decompile /path/to/source/directory /path/to/output/directory
```
Replace /path/to/source/directory and /path/to/output/directory with the appropriate paths.

2 - List Installed Ableton Versions:

You can use the following command to list the Ableton Live versions installed on your system along with their locations:

```bash
abletoolkit list_versions
```

3 - List MIDI Remote Scripts Directories:

Use this command to list the directories where MIDI Remote Scripts are deployed, including the path /Users/${user}/Music/Ableton/User Library/Remote Scripts for macOS:

```bash
abletoolkit list_remote_scripts
```

## Project Files
- README.md: This instruction file.
- requirements.txt: The necessary Python dependencies.
- src/abletoolkit/decompile.py: The main Python script for decompiling.
- src/abletoolkit/cli.py: The CLI client script that aggregates all functionalities.


## Next features
- [ ] live reload of Ableton when midi scripts are updated in specific location