import asyncio

from orchestration.state import ResearchState

from agents.planner_agent import PlannerAgent
from agents.search_agent import SearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.report_agent import ReportAgent

from database.db import SessionLocal

from database.crud import (
    update_status,
    update_report
)

from core.logger import logger


class ResearchWorkflow:

    def __init__(self):

        self.planner = PlannerAgent()

        self.searcher = SearchAgent()

        self.summarizer = SummarizerAgent()

        self.reporter = ReportAgent()

    async def run(
        self,
        query: str,
        report_id: int
    ):

        db = SessionLocal()

        try:

            update_status(
                db,
                report_id,
                "running"
            )

            logger.info(
                f"Research started: {query}"
            )

            state: ResearchState = {
                "query": query,
                "plan": [],
                "search_results": [],
                "summary": "",
                "final_report": ""
            }

            planner_task = asyncio.create_task(
                self.planner.run(query)
            )

            search_task = asyncio.create_task(
                self.searcher.run(query)
            )

            state["plan"] = await planner_task

            logger.info(
                "Planning completed"
            )

            state["search_results"] = await search_task

            logger.info(
                "Search completed"
            )

            state = await self.summarizer.run(
                state
            )

            logger.info(
                "Summary completed"
            )

            state = await self.reporter.run(
                state
            )

            logger.info(
                "Report completed"
            )

            update_report(
                db,
                report_id,
                state["final_report"]
            )

            return state

        except Exception as e:

            update_status(
                db,
                report_id,
                "failed"
            )

            logger.exception(
                str(e)
            )

            raise e

        finally:

            db.close()