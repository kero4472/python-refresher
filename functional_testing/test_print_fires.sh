test -e ssshtest || wget -q \ https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run raw_values python ../print_fires.py \
--country Testland \
--country_column 0 \
--fires_column 2 \
--file_name test_data.csv

assert_in_stdout "[10, 20, 30]"
assert_exit_code 0

run mean_test python ../print_fires.py \
--country Testland \
--country_column 0 \
--fires_column 2 \
--file_name test_data.csv \
--operation mean

assert_in_stdout "20.0"
assert_exit_code 0

run median_test python ../print_fires.py \
--country Testland \
--country_column 0 \
--fires_column 2 \
--file_name test_data.csv \
--operation median

assert_in_stdout "20"
assert_exit_code 0

run std_test python ../print_fires.py \
--country Testland \
--country_column 0 \
--fires_column 2 \
--file_name test_data.csv \
--operation std

assert_in_stdout "8.16496580927726"
assert_exit_code 0

run missing_country python ../print_fires.py \
--country Missingland \
--country_column 0 \
--fires_column 2 \
--file_name test_data.csv

assert_exit_code 1