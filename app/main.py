from fastapi import FastAPI, Response

from app.feedback import router as feedback_router


# FastAPI app
app = FastAPI()

app.include_router(feedback_router.router)

@app.get('/')
def root():
    return Response('<h1>Feedback Generator API.</h1>')
