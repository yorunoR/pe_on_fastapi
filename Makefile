fastapi:
	poetry run uvicorn pe_on_fastapi.main:app --reload

format:
	poetry run pysen run format
