from typing import Optional

from pydantic import BaseModel

from tortoise import models, fields

DEFAULT_MAX_LENGTH_TEXT = 1000
DEFAULT_MAX_LENGTH_MESSAGE = 10000


class TestModel(BaseModel):
    name: str
    message: Optional[str] = None


class UserModel(BaseModel):
    username: str
    password: str


class Test(models.Model):
    name: str = fields.CharField(DEFAULT_MAX_LENGTH_TEXT)
    message: Optional[str] = fields.CharField(DEFAULT_MAX_LENGTH_MESSAGE, null=True)
