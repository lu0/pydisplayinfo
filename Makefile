init:
	virtualenv venv && \
	. venv/bin/activate && \
	pip install -r requirements-dev.txt && \
	pre-commit install

test:
	pytest

build:
	python3 setup.py sdist bdist_wheel
