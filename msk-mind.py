import click
import openapi_client
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration

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
@click.option("--download", is_flag=True, default=False, show_default=True)
def get(ctx, query, download):
    """get the URL to the data bundle that corresponds to the given query.

    QUERY is a SQL select statement
    """
    if (download):
        print(ctx.obj["business"].get_metadata_file_url(query))
    else:
        print(ctx.obj["business"].get_metadata(query))


if __name__ == '__main__':
	cli()
