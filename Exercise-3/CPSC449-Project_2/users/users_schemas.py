from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import List

class User_info(BaseModel):
    uid: int
    name: str
    password: str
    roles: List

class User(BaseModel):
    name: str
    password: str

class User_Role(BaseModel):
    user_id: int
    role_id: int

class Settings(BaseSettings, env_file=".env", extra="ignore"):
    users_database: str
    users_logging_config: str
