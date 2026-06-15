from services.llm_service import LLMService


class SummarizerAgent:

    def __init__(self):
        self.llm = LLMService()

    def run(self, state):

        prompt = f"""
        Summarize:

        {state["search_results"]}
        """

        summary = self.llm.generate(prompt)

        state["summary"] = summary

        return state