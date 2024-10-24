set shell := ["zsh", "-cu"]

default:
  just --list

venv: 
  pip install --upgrade uv
  uv venv --python 3.12.4 \
    && . .venv/bin/activate \
    && uv pip install -r requirements.txt \
    && uv pip install -r requirements-dev.txt

ds:
  . .venv/bin/activate \
    && uv pip install -r requirements-ds.txt

test:
  python -m pytest --doctest-modules ./tests
