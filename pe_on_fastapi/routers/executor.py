import pe_on_fastapi.actions.execution as execution_action
import pe_on_fastapi.schemas.execution as execution_schema
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/execute", response_model=execution_schema.Output)
async def execute(execution_body: execution_schema.Input):
    result, error = execution_action.execute(execution_body)
    return {"result": result}
