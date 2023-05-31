from pathlib import Path

import pytest

from ton_engine.config.file_config_loader import UnsupportedFileFormatError, FileConfigLoader


def test_load_config_json():
    config_loader = FileConfigLoader(
        file_path=Path(__file__).parent / Path('data/sample.json')
    )

    output = config_loader.load_config()

    assert output == {
        "name": "sample.json",
        "value": 1502
    }


def test_load_config_yaml():
    config_loader = FileConfigLoader(
        file_path=Path(__file__).parent / Path('data/sample.yaml')
    )

    output = config_loader.load_config()

    assert output == {
        "name": "sample.yaml",
        "value": 9831
    }


def test_load_config_unsupported_file_format_error():
    config_loader = FileConfigLoader(
        file_path=Path(__file__).parent / Path('data/sample.xml')
    )

    with pytest.raises(UnsupportedFileFormatError):
        config_loader.load_config()
