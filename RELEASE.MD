# Release Process

To make a release, run the 
```sh
make build
```
task, and upload to testpypi and verify.

Ensure that the `__version__` is updated in `./qtrex/__init__.py`
and the `version` tag is updated in `./pyproject.toml`.


```sh
twine upload -r testpypi dist/*
```

Verify the contents at https://test.pypi.org/project/qtrex/

When ready, run
```
twine upload dist/*
```

Using the API tokens.
