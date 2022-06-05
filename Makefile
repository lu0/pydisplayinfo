init:
	virtualenv venv && \
	. venv/bin/activate && \
	pip install -r requirements-dev.txt && \
	pre-commit install

clean-pre-commit-log:
	rm -f .pre-commit.log

test:
	@if [ -f .pre-commit.log ]; then \
		echo "Solve problems in .pre-commit.log"; \
		return 1; \
	else \
		pytest tests; \
	fi

build:
	python3 setup.py sdist bdist_wheel
