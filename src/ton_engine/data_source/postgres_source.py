from sqlalchemy import create_engine, text


class PostgresDataSource:
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

        self._engine = None

    def setup(self):
        """Run setup."""
        self._engine = create_engine(
            f'postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        )

    def run_query(self, query: str) -> list[tuple]:
        """Run query on database and return its result."""
        sql = text(query)

        with self._engine.connect() as connection:
            results = connection.execute(sql)

        return list(results)

    def teardown(self):
        """Close connection."""
        self._engine.dispose()
