# Koyeb Python Hello World

This repository contains a simple example on how to deploy a Python function with
Koyeb. You can simply clone this repository to quickly get started and to experiment with
Koyeb.

Also refer to our [Python Get Started documentation](https://www.koyeb.com/docs/stacks/quickstart/deploy-python-function).

## The Koyeb.yaml file

Deploying a Python function simply requires a `koyeb.yaml` file at the root of
your repository with the instruction about the `runtime` to use and how to
access your function with the `handler` instruction.


## Support of Python dependency engines

Koyeb supports `poetry`, `setup.py`, and `requirements.txt` as tools to manage
your dependencies.

This repository contains `pyproject.toml` file used by `poetry` but `setup.py`
adn `requirements.txt` also picked up automatically.
