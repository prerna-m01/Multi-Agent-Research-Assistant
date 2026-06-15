from services.llm_service import LLMService


class ReportAgent:

    def __init__(self):
        self.llm = LLMService()

    async def run(
        self,
        state
    ):
        prompt = f"""
Create a detailed research report.

Summary:
{state['summary']}
"""

        report = self.llm.generate(prompt)

        state["final_report"] = report

        return state