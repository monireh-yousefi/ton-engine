import click

from ton_engine.data_source.postgres_source import PostgresDataSource


@click.group()
def cli():
    pass


@cli.command()
def start():
    data_source = PostgresDataSource(host='localhost', port=5432, user='postgres', password='postgres', database='mydb')
    data_source.setup()
    results = data_source.run_query('SELECT * FROM students;')
    print(results)
    data_source.teardown()


if __name__ == '__main__':
    cli()
