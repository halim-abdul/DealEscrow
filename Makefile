install:
	python -m pip install -e ".[dev]"

test:
	pytest -q

lint:
	ruff check src api tests

run:
	PYTHONPATH=src uvicorn api.main:app --reload
