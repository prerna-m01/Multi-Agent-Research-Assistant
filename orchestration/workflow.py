from agents.planner_agent import PlannerAgent
from agents.researcher_agent import ResearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.writer_agent import WriterAgent


class ResearchWorkflow:

    def __init__(self):

        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.summarizer = SummarizerAgent()
        self.writer = WriterAgent()

    def run(self, query):

        state = {
            "query": query,
            "plan": [],
            "search_results": [],
            "summary": "",
            "final_report": ""
        }

        state["plan"] = self.planner.run(query)

        state = self.researcher.run(state)

        state = self.summarizer.run(state)

        state = self.writer.run(state)

        return state