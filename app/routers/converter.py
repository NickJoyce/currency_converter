from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import Annotated
from app.schemas.converter import QueryParams
from app.utils.converter import get_result

router = APIRouter()

@router.get("/api/rates")
async def rates(params: Annotated[QueryParams, Depends()]):
    content = await get_result(params.from_, params.to, params.value)
    return JSONResponse(content=content)
