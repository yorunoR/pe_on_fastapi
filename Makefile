fastapi:
	poetry run uvicorn pe_on_fastapi.main:app --port 5000 --reload

format:
	poetry run pysen run format
