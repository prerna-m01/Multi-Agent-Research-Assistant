from google import genai

from core.config import settings


class LLMService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

    def generate(
        self,
        prompt: str
    ):

        try:

            response = (
                self.client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
            )

            return response.text

        except Exception as e:

            return (
                f"LLM Error: {str(e)}"
            )

    def generate_plan(
        self,
        query: str
    ):

        prompt = f"""
Create a research plan for:

{query}

Return ONLY a numbered list.
"""

        try:

            response = (
                self.client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
            )

            plan_text = response.text

            plan = [
                line.strip()
                for line in plan_text.split("\n")
                if line.strip()
            ]

            return plan

        except Exception as e:

            return [
                f"Planning Error: {str(e)}"
            ]