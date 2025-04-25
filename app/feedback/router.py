from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from app.languagemodel import generate_gemini_response
from app.database import db

from .models import FeedbackDocumentModel
from .schemas import FeedbackRequest


router = APIRouter(tags=['feedback'])

@router.post("/feedback/")
async def gen_feedback(feedback: FeedbackRequest):
    try:
        feedback = FeedbackRequest(**feedback.dict())
    except ValidationError as e:
        # Raise an HTTP 422 error if validation fails
        raise HTTPException(status_code=422, detail=e.errors())
    
    prompt = str(feedback)

    response = await generate_gemini_response(prompt)

    # Create a FeedbackDocumentModel instance
    feedback_document = FeedbackDocumentModel(
        request=feedback,
        response=response
    )

    await db["gemini_app"].insert_one(feedback_document.dict(by_alias=True))

    return {"response": response}