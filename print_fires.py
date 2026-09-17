"""
Print fire data for a selected country from a CSV file.

The script accepts command-line arguments for the country name,
the country column, the fire data column, and the input CSV file.
It uses get_column() from my_utils to retrieve the matching fire values.
"""

import argparse
import sys

import my_utils


# Create command-line argument parser.
parser = argparse.ArgumentParser(
    description='Prints the # of fires in a given country from a CSV file.',
    prog='print_fires'
)

# Add country to search for.
parser.add_argument(
    '--country',
    type=str,
    help='The country for which to print fire data.',
    required=True
)

# Add column index containing country names.
parser.add_argument(
    '--country_column',
    type=int,
    help='The index of the country column in the CSV file.',
    required=True
)

# Add column index containing fire data.
parser.add_argument(
    '--fires_column',
    type=int,
    help='The index of the fires column in the CSV file.',
    required=True
)

# Add name of the CSV file to read.
parser.add_argument(
    '--file_name',
    type=str,
    help='The name of the CSV file to read from.',
    required=True
)

# Read the command-line arguments provided by the user.
args = parser.parse_args()

# Store the command-line arguments in variables.
country = args.country
country_column = args.country_column
fires_column = args.fires_column
file_name = args.file_name

# Get the fire values for the selected country.
fires = my_utils.get_column(
    file_name,
    country_column,
    country,
    result_column=fires_column
)

# Exit with an error code if no data was returned.
if len(fires) == 0:
    sys.exit(1)

# Print the resulting list of fire values.
print(fires)
