.PHONY: test
test:
	tox -e py
	open ./htmlcov/index.html

.PHONY: lint
lint:
	tox -e linters

.PHONY: build
build: clean
	python setup.py sdist bdist_wheel

.PHONY: install
install:
	pip install .

.PHONY: clean
clean:
	rm -rf dist
	rm -rf build
