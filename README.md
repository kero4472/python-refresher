# Fire Data Analysis

## Description

This project reads wildfire-related data from a CSV file and reports fire values for a selected country.

The program allows the user to specify the country, the column containing country names, the column containing fire data, and the CSV input file using command-line arguments.

The program can also optionally calculate the mean, median, or standard deviation of the returned fire values.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/kero4472/python-refresher
```

### 2. Create and activate the Mamba environment

Create the environment using the provided `environment.yml` file:

```bash
mamba env create -f environment.yml
```

Activate the environment:

```bash
mamba activate swe4s
```

### 3. Run the example script

```bash
bash run.sh
```

## How to Use

The program is run from the command line using `print_fires.py`.

The available arguments are:

* `--country` - Country to search for
* `--country_column` - Column number containing the country names
* `--fires_column` - Column number containing the fire data
* `--file_name` - Name of the CSV input file


* `--operation` - Optional operation to perform on the fire values: mean, median, or std

### Example

```bash
python print_fires.py \
    --country Afghanistan \
    --country_column 0 \
    --fires_column 2 \
    --file_name Agrofood_co2_emission.csv
```

### To calculate the mean:

```bash
python print_fires.py \
    --country Afghanistan \
    --country_column 0 \
    --fires_column 2 \
    --file_name Agrofood_co2_emission.csv \
    --operation mean
```

## Testing

Unit tests are included for the functions in my_utils.py.

Functional tests are included for print_fires.py using the Stupid Simple Bash Testing framework.

The functional tests check command-line output, operations, and exit codes.

## Version 3.0 Updates

- Added mean, median, and standard deviation functions.
- Added unit tests with positive, negative, and random test cases.
- Added the optional `--operation` argument to `print_fires.py`.
- Added functional tests using the Stupid Simple Bash Testing framework.
- Added test data and exit-code testing.