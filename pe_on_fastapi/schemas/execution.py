from pydantic import BaseModel, Field


class Input(BaseModel):
    code: str
    inputs: str | None = None


class Output(BaseModel):
    result: str
