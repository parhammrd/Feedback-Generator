from datetime import datetime
from pydantic import BaseModel, Field as PydanticField
from bson import ObjectId
from typing import Optional
from .schemas import FeedbackRequest


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, _schema_generator, _field_schema):
        return {"type": "string"}

class FeedbackDocumentModel(BaseModel):
    id: Optional[PyObjectId] = PydanticField(default_factory=PyObjectId, alias="_id")
    time: datetime = PydanticField(default_factory=datetime.utcnow)
    request: FeedbackRequest
    response: str

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str}
    }