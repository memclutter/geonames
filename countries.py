import io
from argparse import ArgumentParser
from urllib.request import urlopen

from sqlalchemy import create_engine
import numpy as np
import pandas as pd

DATA_SOURCE = 'http://download.geonames.org/export/dump/countryInfo.txt'
COLUMNS = [
    'iso',
    'iso3',
    'iso_numeric',
    'fips',
    'country',
    'capital',
    'area',
    'population',
    'continent',
    'tld',
    'currency_code',
    'currency_name',
    'phone',
    'postal_code_format',
    'postal_code_regex',
    'languages',
    'geonameid',
    'neighbours',
    'equivalent_fips_code',
]

COLUMNS_TYPE = {
    'iso': np.str,
    'iso3': np.str,
    'iso_numeric': np.str,
    'fips': np.str,
    'country': np.str,
    'capital': np.str,
    'area': np.float,
    'population': np.int,
    'continent': np.str,
    'tld': np.str,
    'currency_code': np.str,
    'currency_name': np.str,
    'phone': np.str,
    'postal_code_format': np.str,
    'postal_code_regex': np.str,
    'languages': np.str,
    'geonameid': np.int,
    'neighbours': np.str,
    'equivalent_fips_code': np.str,
}

if __name__ == '__main__':
    parser = ArgumentParser(description='Countries list downloader')
    parser.add_argument('--format', default='json', help='Available formats `json`, `sql`')
    parser.add_argument('--query', help='Pandas query expression')
    parser.add_argument('--columns', nargs='+', help='Select columns for result')

    args = parser.parse_args()

    with urlopen(DATA_SOURCE) as response:
        data = response.read().decode('utf-8')

        # Pass description, headers and first char '#'
        csv_data = '\n'.join(data.split('\n')[51:])[1:]

        # Parse csv and write in DataFrame
        df = pd.read_csv(io.StringIO(csv_data), sep='\t', names=COLUMNS, dtype=COLUMNS_TYPE, header=None)

        if args.query is not None:
            df = df.query(args.query)

        # Select columns
        if args.columns is not None and len(args.columns) > 0:
            df = df[args.columns]

        if args.format == 'json':
            print(df.to_json(orient='records'))
        elif args.format == 'sql':
            # TODO dump to sql file
            pass
