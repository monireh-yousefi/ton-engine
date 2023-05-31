from abc import ABC, abstractmethod
from pathlib import Path


class ConfigLoader(ABC):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    @abstractmethod
    def load_config(self):
        pass
