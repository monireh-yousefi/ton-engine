from ton_engine.data_source.sqlalchemy_source import SqlAlchemyDataSource


class PostgresDataSource(SqlAlchemyDataSource):
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        super().__init__(
            url=f'postgresql+psycopg://{user}:{password}@{host}:{port}/{database}',
        )
