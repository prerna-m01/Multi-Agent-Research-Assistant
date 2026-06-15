from services.tavily_service import TavilyService


class SearchAgent:

    def __init__(self):
        self.search_service = TavilyService()

    async def run(
        self,
        query: str
    ):
        return self.search_service.search(query)