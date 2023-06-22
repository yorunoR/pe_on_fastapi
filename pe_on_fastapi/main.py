from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pe_on_fastapi.routers import executor

app = FastAPI()

app.include_router(executor.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
