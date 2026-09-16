import my_utils
import argparse

parser = argparse.ArgumentParser(
    description='Prints the number of fires in a given country from a CSV file.',
    prog='print_fires')

parser.add_argument('--country', 
                    type=str, 
                    help='The country for which to print fire data.',
                    required=True)

parser.add_argument('--country_column',
                    type=int, 
                    help='The index of the country column in the CSV file.',
                    required=True)

parser.add_argument('--fires_column',
                    type=int, 
                    help='The index of the fires column in the CSV file.',
                    required=True)

parser.add_argument('--file_name',
                    type=str,
                    help='The name of the CSV file to read from.',
                    required=True)

args = parser.parse_args()

country = args.country
country_column = args.country_column
fires_column = args.fires_column
file_name = args.file_name

fires = my_utils.get_column(file_name, country_column, country, result_column=fires_column)

print(fires)