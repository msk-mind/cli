import click
import openapi_client
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from util import pprint_ls

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
    """get data that corresponds to the given query.

    QUERY - a SQL select statement.

    DOWNLOAD - an optional flag.
    If the flat is set, return a URL to the query result set.
    """
    if download:
        print(ctx.obj["business"].get_metadata_file_url(query))
    else:
        pprint_ls(ctx.obj["business"].get_metadata(query))


@cli.command()
@click.pass_context
@click.argument("name", required=False)
def table(ctx, name):
    """introspect on available tables and table details.

    NAME - an optional table name.
    If provided, return column details (name, type, comments) for the table.
    """
    result = []
    if name:
        result = ctx.obj["business"].get_metadata("describe " + name)
        pprint_ls([(column['col_name'], column['data_type'], column['comment']) for column in result])
    else:
        result = ctx.obj["business"].get_metadata("show tables")
        pprint_ls([table['tab_name'] for table in result])


if __name__ == '__main__':
	cli()
