from tools.search_tool import SearchTool


class SearchAgent:

    def __init__(self):
        self.search_tool = SearchTool()

    def search(self, query: str):

        return self.search_tool.search(query)