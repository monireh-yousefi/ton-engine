from ton_engine.data_source.postgres_source import PostgresDataSource
from abc import ABC, abstractmethod


class Analysis(ABC):
    def __init__(self, slug: str, datasource: PostgresDataSource):
        self.slug = slug
        self.datasource = datasource

    @abstractmethod
    def run(self):
        pass
