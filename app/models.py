from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    prompts = relationship(
        "PromptHistory",
        back_populates="owner"
    )


class PromptHistory(Base):
    __tablename__ = "prompt_history"

    id = Column(Integer, primary_key=True, index=True)

    user_input = Column(String)
    platform = Column(String)
    style = Column(String)
    optimized_prompt = Column(String)
    quality_score = Column(Integer)

    # For logged-in users
    # Guest users will have NULL here
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    owner = relationship(
        "User",
        back_populates="prompts"
    )