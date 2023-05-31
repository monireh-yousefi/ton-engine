from sqlalchemy import create_engine, text

from ton_engine.data_source.base import DataSource


class SqlAlchemyDataSource(DataSource):
    def __init__(self, url: str):
        self.url = url

        self._engine = None

    def setup(self):
        """Run setup."""
        self._engine = create_engine(self.url)

    def run_query(self, query: str) -> list[tuple]:
        """Run query on database and return its result."""
        sql = text(query)

        with self._engine.connect() as connection:
            results = connection.execute(sql)

        return list(results)

    def teardown(self):
        """Close connection."""
        self._engine.dispose()
