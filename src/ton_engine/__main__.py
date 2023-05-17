from pathlib import Path

import click

from ton_engine.config.config_loader import ConfigLoader


@click.group()
def cli():
    pass


@cli.command()
def start():
    config_loader = ConfigLoader(file_path=Path('./abc.json'))


if __name__ == '__main__':
    cli()
