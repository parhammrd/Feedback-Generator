from google import genai
from google.genai.types import GenerateContentConfig, HttpOptions

from app.settings import GEMINI_API_KEY, LLM_MODEL_NAME


client = genai.Client(api_key=GEMINI_API_KEY)

async def generate_gemini_response(prompt_text: str):
    response = client.models.generate_content(
        model=LLM_MODEL_NAME,
        contents=prompt_text,
        config=GenerateContentConfig(
            system_instruction=[
                "You are a motivational coach for learners in an interactive quiz system.",
                """
                Students interact with five ascending challenge levels:
                Level 1 - Foundational Skills (Easy): Definitions, syntax, recall.
                Level 2 - Comprehension (Easy-Medium): Understanding, logic checking.
                Level 3 - Application (Medium): Problem-solving in context.
                Level 4 - Analysis (Medium-Hard): Debugging, error analysis.
                Level 5 - Synthesis (Hard): Creative, high-order problem design.
                """,
                "Each question has 4 options.",
                # "Each question should be answered in 3 minutes.",
                "Limit the response to 2 sentences."

            ]
        ),
    )

    return response.text
