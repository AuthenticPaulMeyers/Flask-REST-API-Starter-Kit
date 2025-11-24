#!/usr/bin/env bash
# Example: generate a project in the current dir named myapp
python -c "import flask_api_starter; from flask_api_starter.cli import new; import sys; new.callback('myapp')"
