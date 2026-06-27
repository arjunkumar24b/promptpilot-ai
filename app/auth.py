from passlib.context import CryptContext

from fastapi import Depends
from fastapi.security import HTTPBearer
from jose import jwt, JWTError

from .database import SessionLocal
from .models import User
from .security import SECRET_KEY, ALGORITHM


# Password hashing setup
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Hash password
def hash_password(password: str):
    return pwd_context.hash(password)


# Verify password
def verify_password(
        plain_password,
        hashed_password):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# JWT authentication setup
security = HTTPBearer(auto_error=False)


# Mandatory login
def get_current_user(
        credentials=Depends(security)):

    if credentials is None:
        return None

    try:

        token = credentials.credentials

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        db = SessionLocal()

        user = db.query(User).filter(
            User.email == email
        ).first()

        db.close()

        return user

    except JWTError:
        return None


# Optional login (for guest users)
def get_optional_user(
        credentials=Depends(security)):

    return get_current_user(credentials)