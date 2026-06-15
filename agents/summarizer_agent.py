from services.llm_service import LLMService


class SummarizerAgent:

    def __init__(self):
        self.llm = LLMService()

    async def run(
        self,
        state
    ):
        prompt = f"""
Research Topic:
{state['query']}

Search Results:
{state['search_results']}

Create a concise summary.
"""

        summary = self.llm.generate(prompt)

        state["summary"] = summary

        return state