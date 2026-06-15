from pathlib import Path


class ReportStorage:

    def save(self, query: str, report: str):

        reports_dir = Path("reports")

        reports_dir.mkdir(
            exist_ok=True
        )

        filename = query.replace(
            " ",
            "_"
        ).lower()

        file_path = reports_dir / f"{filename}.md"

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        return str(file_path)