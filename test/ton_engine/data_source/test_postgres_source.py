from unittest.mock import patch, Mock, MagicMock

from ton_engine.data_source.postgres_source import PostgresDataSource


def test_setup():
    data_source = PostgresDataSource(
        host='localhost',
        port=5432,
        user='monireh',
        password='p@ssword',
        database='mydb',
    )

    with patch('ton_engine.data_source.postgres_source.create_engine') as create_engine_mock:
        create_engine_mock.return_value = Mock()

        data_source.setup()

        create_engine_mock.assert_called_with("postgresql+psycopg://monireh:p@ssword@localhost:5432/mydb")
        assert data_source._engine == create_engine_mock.return_value


def test_run_query():
    data_source = PostgresDataSource(
        host='localhost',
        port=5432,
        user='monireh',
        password='p@ssword',
        database='mydb',
    )

    expected_output = [('a', 'b'), ('c', 'd')]

    connection_mock = Mock()
    connection_mock.execute = Mock(return_value=expected_output)

    data_source._engine = Mock()
    data_source._engine.connect = Mock(return_value=MagicMock())
    data_source._engine.connect.return_value.__enter__ = Mock(return_value=connection_mock)

    with patch('ton_engine.data_source.postgres_source.text') as text_mock:
        text_mock.return_value = Mock()

        output = data_source.run_query('select *')

        connection_mock.execute.assert_called_with(text_mock.return_value)

    assert output == expected_output


def test_teardown():
    data_source = PostgresDataSource(
        host='localhost',
        port=5432,
        user='monireh',
        password='p@ssword',
        database='mydb',
    )
    data_source._engine = Mock()

    data_source.teardown()

    data_source._engine.dispose.assert_called()
