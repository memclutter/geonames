# geonames

My scripts, parser and tools for working with the geonames free Gazetteer data source. 

Data source http://download.geonames.org/export/dump/

## Features

- Download country info list from geonames
- Convert to `json` and `sql`
- Select the necessary columns
- Friendly syntax filtering
- Easy sorting

## Motivation

Many projects need a list of countries. There is also a need for pre-filtering data, for example, to select only countries with a population of more than 10m or countries of Europe.

Also, different projects require different formats, for example `json`, `sql` and `xml`.

The goal of this project is to create a number of scripts to generate such lists of countries.

I hope someone will like it. I also hope someone writes recommendations and feature requests.

## Examples

Get a list of countries in json format

```
python countries.py --format json 
```

Get a list of countries in sql format (inserts)

```
python countries.py --format sql --table countries
```

Select only columns `iso` and `country`

```
python countries.py --format json --columns iso country
```

Filter out countries with population over 125 000 000

```
python countries.py --format json --query 'population>=125000000' --columns iso country population
```

Sorting by population (DESC)

```
python countries.py --format json --sort 'population-' --columns iso country population
```

For help run

```
python countries.py -h
```
