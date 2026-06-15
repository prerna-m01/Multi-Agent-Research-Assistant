from services.llm_service import LLMService


class PlannerAgent:

    def __init__(self):
        self.llm = LLMService()

    async def run(
        self,
        query: str
    ):
        return self.llm.generate_plan(query)