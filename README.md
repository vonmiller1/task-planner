# AI Agent Task Planner

A lightweight Python command-line application that turns a project goal into a practical checklist, with optional note lookup and an explicit-hours estimate.

## Overview

Task Planner demonstrates a small, inspectable agent workflow without external AI services or framework dependencies. It selects from three local tools: searches the project notes for relevant lines, calculates a work estimate when the goal states a days-and-hours-per-day relationship, and creates a checklist tailored to recognized project terms.

## Features

- Generates a starter checklist from a natural-language goal.
- Adds focused RAG and API implementation steps when those terms are present.
- Searches `data/notes.txt` for relevant notes when the goal mentions supported topics.
- Calculates an estimate from explicit phrasing such as `3 days at 4 hours per day`.
- Rejects empty or too-short goals with a clear CLI error.
- Uses only the Python standard library; no network calls or API keys are required.

## Tech stack

- Python
- Python standard library (`argparse`, `pathlib`, `re`, and `unittest`)

## Prerequisites

- Python 3.8 or newer

No third-party packages are required.

## Getting started

Clone the repository and change into its directory:

```bash
git clone https://github.com/vonmiller1/task-planner.git
cd task-planner
```

There are no dependency installation steps or environment variables. The optional notes source is `data/notes.txt`, resolved relative to the project rather than the shell's current directory.

## Running locally

Pass a goal with `--goal`:

```bash
python main.py --goal "Plan a small RAG project and estimate 3 days at 4 hours per day"
```

The CLI prints the goal, selected tools, numbered checklist, and any matching notes. Run `python main.py --help` to see the command-line usage.

## Testing

The test suite uses `unittest` and can be run with:

```bash
python -m unittest discover -s tests
```

## Project structure

| Path | Purpose |
| --- | --- |
| `main.py` | Command-line entry point and result presentation |
| `src/agent.py` | Goal validation, tool selection, and workflow orchestration |
| `src/tools.py` | Note search, estimate calculation, and checklist generation |
| `src/errors.py` | Goal validation and shared task-planner exceptions |
| `src/config.py` | Defaults and JSON-backed configuration helper |
| `src/logger.py` | Optional logging setup helper |
| `data/notes.txt` | Local reference notes used by note search |
| `config.json.example` | Sample JSON settings for `ConfigManager` |
| `tests/` | Unit tests |

## Configuration

The command-line application currently runs without a configuration file. `src/config.py` provides a `ConfigManager` with defaults for tool limits, logging, and note storage, but those settings are not currently connected to the CLI workflow. Copy `config.json.example` to `config.json` if you want to experiment with the helper locally. No environment variables are read.

## Deployment

The project has no container, deployment scripts, or hosted service configuration. It can be run directly with Python in an environment that has the repository files.

## Contributing

Fork the repository, create a focused branch, and submit a pull request describing the change. Keep changes small and add or update `unittest` coverage for behavior changes.

## License

No `LICENSE` file is present in this repository. Please check the repository owner’s licensing terms before reuse.
