#!/bin/zsh

python3 -m venv venv

pip install .

echo 'export PATH="$PWD/venv/bin:$PATH"' >> ~/.zshrc

# shellcheck disable=SC1090
source ~/.zshrc