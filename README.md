# Notes CLI

## Overview
A simple command-line note manager. Notes are stored locally in a JSON file. The project is split into three layers: storage, business logic, and CLI.

## Requirements
Python 3.10+

## Installation
```
git clone <your-repo-url>
cd task
```

## Usage
```
python main.py <command>
```

## Supported Commands

* `notes add <title> <content>`: Creates a new note with the given title and content.
* `notes list`: Displays all saved notes.
* `notes show <id>`: Displays the note with the specified ID. If the ID does not exist, an error message is shown.
* `notes delete <id>`: Deletes the note with the specified ID. If the ID does not exist, an error message is shown.
* `notes --help`: Shows usage information.

## Examples
```
python main.py add "One" "Two"
python main.py list
python main.py show 1
python main.py delete 1
```

## Running Tests
```
python tests/tests_notes.py
```

## Project Structure
```
task/
├── main.py            # CLI layer
├── notes_logic.py     # Business logic
├── notes_manager.py   # Storage layer (JSON)
├── notes.json         # Created automatically on first run
└── tests/
    └── tests_notes.py # Unit tests
```