class ResearchAgent:

    def run(self, state):
        results = []

        for topic in state["plan"]:
            results.append({
                "topic": topic,
                "content": f"Research about {topic}"
            })

        state["search_results"] = results

        return state