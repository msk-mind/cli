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

    QUERY - SQL select statement.

    :returns: domain metadata.
    """
    print_mind_response(ctx.obj["business"].get_metadata(query))


@cli.command()
@click.pass_context
@click.argument("query")
def download_metadata(ctx, query):
    """download domain metadata.

    QUERY - SQL select statement.

    :returns: link to download the data bundle.
    """
    print_mind_response(ctx.obj["business"].get_metadata_url(query))


@cli.command()
@click.pass_context
@click.argument("query")
def files(ctx, query):
    """query operational metadata.

    QUERY - Atlas DSL query.

    :returns: operational metadata.
    """
    print_mind_response(ctx.obj["op"].get_files(query))


@cli.command()
@click.pass_context
@click.argument("query")
def download_files(ctx, query):
    """download operational metadata.

    QUERY - Atlas DSL query.

    :returns: link to download the data bundle.
    """
    print_mind_response(ctx.obj["op"].get_file_url(query))


@cli.command()
@click.pass_context
def list_databases(ctx):
    """show available databases.

    :returns: list of available databases.
    """
    res = ctx.obj["op"].get_files("from hive_db where name != 'default' and __state='ACTIVE' select name")
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
    query = "".join(["from hive_table where db.name = '",
                     db,
                     "' and __state='ACTIVE' select name, comment"])
    res = ctx.obj["op"].get_files(query)
    if res.status == 'OK':
        data = [[x['name'], str(x['comment'])] for x in res.payload]
        header = ['name', 'comment']
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
    query = "".join(["from hive_column where table.name = '",
                     table,
                     "' and table.db.name = '",
                     db,
                     "' and __state='ACTIVE' select name, type, comment"])
    res = ctx.obj["op"].get_files(query)
    if res.status == 'OK':
        data = [[x['name'], x['type'], str(x['comment'])] for x in res.payload]
        header = ['name', 'type', 'comment']
        pprint_table(data, header)
    else:
        print_mind_response(res)


if __name__ == '__main__':
	cli()
