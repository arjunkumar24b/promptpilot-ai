from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from datetime import datetime

from .database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        index=True
    )

    email = Column(
        String,
        unique=True,
        index=True
    )

    password = Column(String)


class PromptHistory(Base):

    __tablename__ = "prompt_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_input = Column(Text)

    platform = Column(String)

    style = Column(String)

    optimized_prompt = Column(Text)

    quality_score = Column(Integer)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )