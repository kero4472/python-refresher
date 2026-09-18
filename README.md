# Fire Data Analysis

## Description

This project reads wildfire-related data from a CSV file and reports fire values for a selected country.

The program allows the user to specify the country, the column containing country names, the column containing fire data, and the CSV input file using command-line arguments.

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
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

### Example

```bash
python print_fires.py \
    --country Afghanistan \
    --country_column 0 \
    --fires_column 2 \
    --file_name Agrofood_co2_emission.csv
```
