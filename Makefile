init:
	virtualenv venv && \
	. venv/bin/activate && \
	pip install -r requirements-dev.txt && \
	pre-commit install -t pre-commit -t pre-push

test:
	pytest

build:
	python3 setup.py sdist bdist_wheel
