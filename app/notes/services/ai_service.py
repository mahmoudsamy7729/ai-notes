from huggingface_hub import InferenceClient
from openai import OpenAI
from app.core.config import settings


# ✅ Your Hugging Face API key (must be added to settings)
HUGGINGFACE_API_KEY = settings.huggingface_api_key


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HUGGINGFACE_API_KEY,
)


system_message = """
You are an AI assistant specialized in summarizing notes.  
Your task is to read the user's notes and generate a clear, concise, and well-structured summary.

Rules to Follow:
- Provide a short and meaningful summary.
- Include only the most important ideas, actions, or decisions.
- Remove unnecessary details, repetition, and filler content.
- If the notes are messy, organize them logically (bullet points, headings).
- If key information is missing or unclear, indicate it as: (missing info).
- Use a neutral, professional tone.

Output Format:
Summary:
- Point 1…
- Point 2…
- Action items (if any)…
- Decisions or results…
"""

class AIService:
    @staticmethod
    async def summarize_notes(note: str) :
        completion = client.chat.completions.create(
            model="zai-org/GLM-4.6:novita",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": note}        
            ],
            #stream = True
        )

        # for chunk in completion:
        #     content = chunk.choices[0].delta.content or ""
        #     yield content

        return (completion.choices[0].message.content)
