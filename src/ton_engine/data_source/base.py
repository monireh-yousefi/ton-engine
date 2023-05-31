from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def setup(self):
        """Run setup."""
        pass

    @abstractmethod
    def run_query(self, query: str) -> list[tuple]:
        """Run query on database and return its result."""
        pass

    @abstractmethod
    def teardown(self):
        """Close connection."""
        pass
