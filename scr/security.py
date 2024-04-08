from settings import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# secret em bcrypt - $2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW
# bolinhas em bcrypt - $2b$12$5lY1RPNbyFHP2bK/JjjY0eyiIJnmxUfUE0OHi81xg2nN1w1NoKznK
db_clientes_api = {
    "abc": {
        "username": "abc",
        "full_name": "Abc dos Testes",
        "email": "abc@example.com",
        "password": "$2b$12$5lY1RPNbyFHP2bK/JjjY0eyiIJnmxUfUE0OHi81xg2nN1w1NoKznK",
        "disabled": False,
    },
    "bolinhas": {
        "username": "bolinhas",
        "full_name": "Bolinhas dos Testes",
        "email": "bolinhas@example.com",
        "password": "$2b$12$5lY1RPNbyFHP2bK/JjjY0eyiIJnmxUfUE0OHi81xg2nN1w1NoKznK",
        "disabled": True,
    },
}

class Token(BaseModel):
    access_token: str
    token_tipo: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # cifra da senha do usuário
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # token

def verify_password(plain_password, password):
    return pwd_context.verify(plain_password, password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user