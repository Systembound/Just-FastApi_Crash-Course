from os import getenv

from fastapi import FastAPI, Security, Depends
from tortoise import Tortoise

from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from fastapi.exceptions import HTTPException

from src.models import TestModel, Test, UserModel

app = FastAPI()
security_access = JwtAccessBearer("asjdasjsajdajd", auto_error=True)


async def db_init():
    await Tortoise.init(
        db_url=getenv("DB_URL"),
        modules={
            "models": ["src.models"]
        }
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()


@app.on_event("startup")
async def init():
    # initialize database
    await db_init()


@app.on_event("shutdown")
async def close():
    # close db connections
    await close_db()


@app.post("/auth")
def auth(user: UserModel):
    subject = {
        "username": user.username
    }
    access_token, refresh_token = security_access.create_access_token(
        subject=subject
    ), security_access.create_refresh_token(subject=subject)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


@app.get("/me")
def current_user(creds: JwtAuthorizationCredentials = Security(security_access)):
    if not creds:
        raise HTTPException(
            401,
            "invalid Authorization Token!"
        )

    return {
        "username": creds["username"]
    }


@app.get("/")
async def index():
    return {
        "message": "hello"
    }


@app.post("/test")
async def test(req: TestModel):
    # validated, nice and clean
    test_model = Test(**req.dict())
    await test_model.save()

    return {
        "success": True,
        "test": test_model,
    }
