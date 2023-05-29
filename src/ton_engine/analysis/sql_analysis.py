from pathlib import Path

from ton_engine.analysis.base import Analysis
from ton_engine.data_source.postgres_source import PostgresDataSource


class SQLAnalysis(Analysis):
    def __init__(self, slug: str, datasource: PostgresDataSource, sql_file_path: Path):
        super().__init__(
            slug=slug,
            datasource=datasource
        )
        self.sql_file_path = sql_file_path

    def run(self):
        query = self.sql_file_path.read_text()
        return self.datasource.run_query(query=query)
