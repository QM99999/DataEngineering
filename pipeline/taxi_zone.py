#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine

URL = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'


@click.command()
@click.option('--pg-user', type=str, default='root', help='PostgreSQL username')
@click.option('--pg-pass', type=str, default='root', help='PostgreSQL password')
@click.option('--pg-host', type=str, default='localhost', help='PostgreSQL host')
@click.option('--pg-port', type=str, default='5432', help='PostgreSQL port')
@click.option('--pg-db', type=str, default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', type=str, default='taxi_zones', help='Target table name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):
    """Ingest NYC taxi zone lookup CSV into PostgreSQL database."""
    engine = create_engine(f'postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    df = pd.read_csv(URL)

    df.head(0).to_sql(
        name=target_table,
        con=engine,
        if_exists='replace',
        index=False,
    )

    df.to_sql(
        name=target_table,
        con=engine,
        if_exists='append',
        index=False,
    )


if __name__ == '__main__':
    run()