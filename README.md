# Feedback Generator

This project is a FastAPI-based application that generates feedback using Gemini. 

## Prerequisites

**Gemini API Key**: You need a Gemini API key to use the Gemini API. Update the `GEMINI_API_KEY` in the `.env` file with your API key.

**MongoDB**: You need a running MongoDB instance. Update the `MONGODB_URL` in the `.env` file to point to your MongoDB instance. Also, create a database and collection name as well.

Tip: You can deactivate the MongoDB by comment out the following line in `app/router.py` to avoid database-related errors:

```python
await db["gemini_app"].insert_one(feedback_document.dict(by_alias=True))
```

## Setup and Deployment

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Feedback-Generator
   ```

2. install the required packages (Use virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

3. run the server:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

## API Requests

### Example Request

```
POST /feedback/
Content-Type: application/json

{
  "student_data": {
    "question_index": "#Q15",
    "question_level": "Medium-Hard",
    "time_spent": "13 minutes",
    "attempts": "2, all correct",
    "prior_performance": "Good on Level 5"
  },
  "objective": "Generate a short feedback message that promotes a growth mindset and helps the student stay motivated.",
  "persuasive_strategies": "Social Comparison",
  "tone": "Growth mindset"
}
```

### Example Response
```
{
    "response": "Even though this was a tough question, you didn't give up, and your persistence paid off! Think of how much you've grown since the earlier levels; you're tackling challenges that once seemed daunting with increasing confidence.\n"
}