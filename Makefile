init:
	virtualenv venv && . venv/bin/activate && \
	python3 -m pip install --upgrade pip && \
	python3 -m pip install -r requirements-dev.txt && \
	pre-commit install -t pre-commit -t pre-push

test:
	pytest

build:
	python3 setup.py sdist bdist_wheel
