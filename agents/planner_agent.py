from services.llm_service import LLMService


class PlannerAgent:

    def __init__(self):
        self.llm = LLMService()

    def create_plan(self, query: str):

        return self.llm.generate_plan(query)