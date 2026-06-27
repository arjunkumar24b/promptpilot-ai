from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .schemas import (
    PromptRequest,
    UserCreate,
    UserLogin
)

from .gemini_service import generate_prompt
from .database import SessionLocal, engine

from .models import (
    Base,
    PromptHistory,
    User
)

from .crud import save_prompt
from .scorer import calculate_score

from .auth import (
    hash_password,
    verify_password,
    get_optional_user,
    get_current_user
)

from .security import create_access_token

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PromptPilot AI",
    version="8.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- ROOT ---------------- #

@app.get("/")
def root():
    return {
        "message": "Welcome to PromptPilot AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ---------------- USER AUTH ---------------- #

@app.post("/signup")
def signup(user: UserCreate):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        db.close()

        return {
            "message": "User already exists"
        }

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return {
        "message": "User created successfully"
    }


@app.post("/login")
def login(user: UserLogin):

    db = SessionLocal()

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        db.close()

        return {
            "message": "Invalid credentials"
        }

    if not verify_password(
            user.password,
            db_user.password):

        db.close()

        return {
            "message": "Invalid credentials"
        }

    # Create JWT token
    access_token = create_access_token(
        data={
            "sub": db_user.email
        }
    )

    db.close()

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ---------------- PROMPT OPTIMIZATION ---------------- #




@app.post("/optimize")
def optimize(
    request: PromptRequest,
    current_user=Depends(get_optional_user)
):

    result = generate_prompt(
        request.user_input,
        request.platform,
        request.style
    )

    quality_score = calculate_score(
        request.user_input
    )

    db = SessionLocal()

    save_prompt(
        db=db,
        user_input=request.user_input,
        platform=request.platform,
        style=request.style,
        optimized_prompt=result,
        quality_score=quality_score,
        user_id=current_user.id if current_user else None
    )

    db.close()

    return {
        "result": result,
        "quality_score": quality_score,
        "saved": current_user is not None
    }
# ---------------- HISTORY ---------------- #

@app.get("/history")
def history(
    current_user=Depends(get_current_user)
):

    if current_user is None:
        return {
            "message":
            "Please login to access your prompt history."
        }

    db = SessionLocal()

    records = db.query(
        PromptHistory
    ).filter(
        PromptHistory.user_id == current_user.id
    ).all()

    db.close()

    return records


@app.delete("/history/{prompt_id}")
def delete_history(prompt_id: int):

    db = SessionLocal()

    record = db.query(
        PromptHistory
    ).filter(
        PromptHistory.id == prompt_id
    ).first()

    if not record:
        db.close()

        return {
            "message": "Prompt not found"
        }

    db.delete(record)
    db.commit()

    db.close()

    return {
        "message": "Prompt deleted successfully"
    }


# ---------------- SEARCH ---------------- #

@app.get("/search")
def search_prompts(query: str):

    db = SessionLocal()

    records = db.query(
        PromptHistory
    ).filter(
        PromptHistory.user_input.contains(query)
    ).all()

    db.close()

    return records


# ---------------- ANALYTICS ---------------- #

@app.get("/analytics")
def analytics():

    db = SessionLocal()

    prompts = db.query(
        PromptHistory
    ).all()

    total_prompts = len(prompts)

    if total_prompts == 0:
        average_score = 0
    else:
        average_score = sum(
            p.quality_score or 0
            for p in prompts
        ) / total_prompts

    db.close()

    return {
        "total_prompts": total_prompts,
        "average_quality_score": round(
            average_score, 2
        )
    }