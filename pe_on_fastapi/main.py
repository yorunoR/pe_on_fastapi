from fastapi import FastAPI
from pe_on_fastapi.routers import executor

app = FastAPI()
app.include_router(executor.router)
