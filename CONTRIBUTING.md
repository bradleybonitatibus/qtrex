# Contibuting Guide

Welcome to the `qtrex` contributing guide!

To get started, you'll want to setup a fresh `venv` with

```sh
python3 -m venv venv
source venv/bin/activate
```
and then install the `dev-requirements.txt`, which is compiled by `pip-compile`
and install the `pre-commit` hooks
```sh
pip3 install dev-requirements.txt
pre-commit install
```
to ensure all the hooks are run before committing code.
