.PHONY: lint
lint:
	python -m pylint --version
	python -m pylint app/

.PHONY: test
test:
	python -m pytest --version
	python -m pytest app/tests/

.PHONY: black
black:
	python -m black --version
	python -m black .

.PHONY: ci
ci: precommit lint test
