from google import genai
from core.config import settings


class LLMService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

    def generate_plan(self, query: str):

        prompt = f"""
        Create a research plan for:

        {query}

        Return ONLY a numbered list.
        Example:

        1. Understand the topic
        2. Collect information
        3. Analyze findings
        4. Create report
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        plan_text = response.text

        plan_list = [
            line.strip()
            for line in plan_text.split("\n")
            if line.strip()
        ]

        return plan_list