.PHONY: type-check

type-check:
	poetry run mypy --explicit-package-bases src
