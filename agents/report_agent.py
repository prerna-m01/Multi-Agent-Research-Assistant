from services.llm_service import LLMService
from services.report_storage import ReportStorage


class ReportAgent:

    def __init__(self):

        self.llm = LLMService()

        self.storage = ReportStorage()

    def run(self, state):

        prompt = f"""
        Create a detailed research report.

        Topic:
        {state['query']}

        Summary:
        {state['summary']}
        """

        report = self.llm.generate(
            prompt
        )

        state["final_report"] = report

        report_path = self.storage.save(
            state["query"],
            report
        )

        state["report_path"] = report_path

        return state