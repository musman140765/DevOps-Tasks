# File Monitoring Script

## Overview

This Python script monitors a specified directory for file creation, deletion, and modification events. All changes are logged into a `log.txt` file.

## Features

- Logs the following file events:
  - Creation
  - Deletion
  - Modification
- Uses the `watchdog` library for efficient monitoring.
- Runs indefinitely until manually stopped.

## Prerequisites

- Python 3
- `watchdog` Python module

## Installation

```bash
pip install -r requirements.txt
