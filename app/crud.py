from sqlalchemy.orm import Session
from .models import PromptHistory


def save_prompt(
        db: Session,
        user_input,
        platform,
        style,
        optimized_prompt,
        quality_score):

    record = PromptHistory(
        user_input=user_input,
        platform=platform,
        style=style,
        optimized_prompt=optimized_prompt,
        quality_score=quality_score
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record