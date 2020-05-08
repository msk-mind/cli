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
    ctx.obj["query"] = openapi_client.QueryApi(client)
    ctx.obj["introspect"] = openapi_client.IntrospectApi(client)


@cli.command()
@click.pass_context
@click.argument("query")
def query(ctx, query):
    """query data.

    QUERY - SQL select statement or Atlas DSL string.

    :returns: domain metadata.
    """
    print_mind_response(ctx.obj["query"].query(query))


@cli.command()
@click.pass_context
@click.argument("query")
def download(ctx, query):
    """download data.

    QUERY - SQL select statement or Atlas DSL string.

    :returns: link to download the data bundle.
    """
    print_mind_response(ctx.obj["query"].download(query))


@cli.command()
@click.pass_context
def list_databases(ctx):
    """show available databases.

    :returns: list of available databases.
    """
    res = ctx.obj["introspect"].get_databases()
    if res.status == 'OK':
        pprint_ls([x['name'] for x in res.payload])
    else:
        print_mind_response(res)

@cli.command()
@click.pass_context
@click.argument("db")
def list_tables(ctx, db):
    """show available tables given a database.

    DB - database name.

    :returns: list of table names and comments
    """
    res = ctx.obj["introspect"].get_tables(db)
    if res.status == 'OK':
        data = [[x['name'], str(x['comment'])] for x in res.payload]
        header = ['name', 'description']
        pprint_table(data, header)
    else:
        print_mind_response(res)


@cli.command()
@click.pass_context
@click.argument("db")
@click.argument("table")
def list_columns(ctx, db, table):
    """show available columns given database and table.

    DB - database name.

    TABLE - table name in the database.

    :returns: list of column names and comments
    """
    res = ctx.obj["introspect"].get_columns(db, table)
    if res.status == 'OK':
        data = [[x['name'], x['type'], str(x['comment'])] for x in res.payload]
        header = ['name', 'type', 'description']
        pprint_table(data, header)
    else:
        print_mind_response(res)


if __name__ == '__main__':
	cli()
