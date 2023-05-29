from pathlib import Path
from unittest.mock import Mock

from ton_engine.analysis.sql_analysis import SQLAnalysis


def test_run():
    datasource_mock = Mock()
    datasource_mock.run_query = Mock(return_value=['1', '2'])

    sql_analysis = SQLAnalysis(
        slug='abc',
        datasource=datasource_mock,
        sql_file_path=Path(__file__).parent / Path('data/sample.sql'),
    )

    result = sql_analysis.run()

    datasource_mock.run_query.assert_called_with(query="SELECT *\nFROM Students;")

    assert result == ['1', '2']
