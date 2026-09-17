# #!/bin/bash

# Example 1: valid run
python print_fires.py \
    --country Afghanistan \
    --country_column 0 \
    --fires_column 2 \
    --file_name Agrofood_co2_emission.csv

# Example 2: error - file does not exist
python print_fires.py \
    --country Afghanistan \
    --country_column 0 \
    --fires_column 2 \
    --file_name does_not_exist.csv

# Example 3: error - missing required fires_column argument
python print_fires.py \
    --country Afghanistan \
    --country_column 0 \
    --file_name Agrofood_co2_emission.csv