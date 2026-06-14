class WriterAgent:

    def write_report(self, query, results):
        report = f"# Research Report\n\nTopic: {query}\n\n"

        for result in results:
            report += f"- {result['content']}\n"

        return report