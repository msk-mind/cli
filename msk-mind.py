import click
import openapi_client
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from util import *

@click.group()
@click.pass_context
@click.option('--host', default="http://localhost:8080", show_default=True)
def cli(ctx, host):
    """Welcome to MSK MIND!
    """
    if ctx.obj is None:
        ctx.obj = dict()
    # setup api client
    config = Configuration(host=host)
    client = ApiClient(configuration=config)
    ctx.obj["business"] = openapi_client.BusinessApi(client)
    ctx.obj["op"] = openapi_client.OperationApi(client)


@cli.command()
@click.pass_context
@click.argument("query")
def metadata(ctx, query):
    """query domain metadata.

    QUERY - a SQL select statement.
    """
    print_mind_reponse(ctx.obj["business"].get_metadata(query))


@cli.command()
@click.pass_context
@click.argument("query")
def download_metadata(ctx, query):
    """download domain metadata.

    QUERY - a SQL select statement.
    """
    print_mind_reponse(ctx.obj["business"].get_metadata_url(query))


@cli.command()
@click.pass_context
@click.argument("query")
def files(ctx, query):
    """query operational metadata.

    QUERY - Atlas DSL query.
    """
    print_mind_reponse(ctx.obj["op"].get_files(query))


@cli.command()
@click.pass_context
@click.argument("query")
def download_files(ctx, query):
    """download operational metadata.

    QUERY - Atlas DSL query.
    """
    print_mind_reponse(ctx.obj["op"].get_file_url(query))


if __name__ == '__main__':
	cli()
