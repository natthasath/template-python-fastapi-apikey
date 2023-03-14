from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKey
from app.middleware.auth import get_api_key

router = APIRouter(
    prefix="/template",
    tags=["TEMPLATE"],
    responses={404: {"message": "Not found"}}
)

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/locked")
async def locked(api_key: APIKey = Depends(get_api_key)):
    return {"message": "Hello World"}