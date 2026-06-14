from agent.planner_agent import PlannerAgent
from agent.research_agent import ResearchAgent
from agent.writer_agent import WriterAgent


class ResearchWorkflow:

    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.writer = WriterAgent()

    def run(self, query):

        plan = self.planner.generate_plan(query)

        results = self.researcher.search(query)

        report = self.writer.write_report(query, results)

        return {
            "plan": plan,
            "report": report
        }