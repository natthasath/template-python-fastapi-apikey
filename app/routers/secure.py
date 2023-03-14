from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKey
from fastapi.params import Security
from app.middleware.auth import get_api_key

router = APIRouter(
    prefix="/secure",
    tags=["SECURE"],
    responses={404: {"message": "Not found"}},
    dependencies=[Security(get_api_key)]
)

@router.get("/dog")
async def dog():
    return {"message": "Hello World"}

@router.get("/cat")
async def cat():
    return {"message": "Hello World"}