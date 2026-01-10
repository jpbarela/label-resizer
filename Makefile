.PHONY: type-check

type-check:
	poetry run mypy src
