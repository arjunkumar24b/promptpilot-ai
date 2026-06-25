from pydantic import BaseModel


class PromptRequest(BaseModel):
    user_input: str
    platform: str
    style: str


class PromptResponse(BaseModel):
    category: str
    optimized_prompt: str
    tips: list[str]


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str