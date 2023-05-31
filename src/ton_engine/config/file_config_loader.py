import json
from pathlib import Path

import yaml

from ton_engine.config.base import ConfigLoader


class UnsupportedFileFormatError(Exception):
    pass


class FileConfigLoader(ConfigLoader):
    def __init__(self, file_path: Path):
        super().__init__(
            file_path=file_path
        )

    def load_config(self) -> dict:
        """Loads config from json and yaml files."""
        if self.file_path.suffix == '.json':
            return json.loads(self.file_path.read_text())

        if self.file_path.suffix in {'.yaml', '.yml'}:
            return yaml.safe_load(self.file_path.read_text())

        raise UnsupportedFileFormatError(f"Unsupported config file format: `{self.file_path.suffix}`!")
