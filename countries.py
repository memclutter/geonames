from csv import DictReader, QUOTE_NONE, reader
import io
from argparse import ArgumentParser
from urllib.request import urlopen

from pandas import read_csv


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
    'currency_ame',
    'phone',
    'postal_code_format',
    'postal_code_regex',
    'languages',
    'geonameid',
    'neighbours',
    'equivalent_fips_code',
]

if __name__ == '__main__':
    parser = ArgumentParser(description='Countries list downloader')
    parser.add_argument('--format', default='json', help='Available formats `json`, `sql`')

    args = parser.parse_args()

    with urlopen(DATA_SOURCE) as response:
        data = response.read().decode('utf-8')

        # Pass description and first char '#'
        csv_data = '\n'.join(data.split('\n')[51:])[1:]

        # Parse csv and write in DataFrame
        df = read_csv(io.StringIO(csv_data), sep='\t', names=COLUMNS, header=None)

        # TODO iterate data frame and filter

