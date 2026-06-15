from orchestration.state import ResearchState

from agents.planner_agent import PlannerAgent
from agents.search_agent import SearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.report_agent import ReportAgent

from database.db import SessionLocal
from database.crud import save_research
from core.logger import logger

logger.info(f"Research started: {query}")
logger.info("Planning completed")
logger.info("Search completed")
logger.info("Summary completed")
logger.info("Report completed")


class ResearchWorkflow:

    def __init__(self):

        self.planner = PlannerAgent()
        self.searcher = SearchAgent()
        self.summarizer = SummarizerAgent()
        self.reporter = ReportAgent()

    def run(self, query: str):

        state: ResearchState = {
            "query": query,
            "plan": [],
            "search_results": [],
            "summary": "",
            "final_report": ""
        }

        state["plan"] = self.planner.run(query)

        state["search_results"] = self.searcher.run(query)

        state = self.summarizer.run(state)

        state = self.reporter.run(state)

        db = SessionLocal()

        save_research(
            db=db,
            query=query,
            report=state["final_report"]
        )

        db.close()

        return state