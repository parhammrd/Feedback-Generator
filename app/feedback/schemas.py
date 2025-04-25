from typing import Optional
from pydantic import BaseModel
from enum import Enum


class QuestionLevelEnum(str, Enum):
    level_1 = "Easy"
    level_2 = "Easy-Medium"
    level_3 = "Medium"
    level_4 = "Medium-Hard"
    level_5 = "Hard"

class StudentData(BaseModel):
    question_index: Optional[str]
    question_level: QuestionLevelEnum
    time_spent: str
    attempts: str
    prior_performance: str

    def __str__(self) -> str:
        return f"""Student behavior data:
        Question: {self.question_index}
        Question Level: {self.question_level}
        Time Spent: {self.time_spent}
        Attempts: {self.attempts}
        Prior level performance: {self.prior_performance}"""

class FeedbackRequest(BaseModel):
    student_data: StudentData
    objective: str
    persuasive_strategies : str
    tone: str

    def __str__(self) -> str:
        return f"""Feedback request:
        {self.objective}
        Please present a persuasive {self.persuasive_strategies} with a {self.tone} tone.
        Student Data: {self.student_data}"""
