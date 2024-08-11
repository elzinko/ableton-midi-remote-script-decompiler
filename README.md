# AbleToolKit

## Description
This project is a small utility for Ableton midi remote scripts developers.
Here are examples of functionnalities it provides :
- list all Ableton Live installed versions
- list all Ableton midi remote scripts locations
- get a pyc file python's version
- decompile the some python files into a specifi location

## Installation

```bash
make install
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

1 - List Installed Ableton Versions:

You can use the following command to list the Ableton Live versions installed on your system along with their locations:

```bash
abletoolkit list_versions
```

2 - List MIDI Remote Scripts Directories:

Use this command to list the directories where MIDI Remote Scripts are deployed, including the path /Users/${user}/Music/Ableton/User Library/Remote Scripts for macOS:

```bash
abletoolkit list_remote_scripts
```

3 - Get a pyc file Python's version:

To get the python version of a .pyc file:

```bash
abletoolkit version /path/to/pyc/file
```

4 - Decompile a script:

To decompile some scripts:

```bash
abletoolkit decompile /path/to/source/directory /path/to/output/directory
```


## Next features
- [ ] live reload of Ableton when midi scripts are updated in specific location
