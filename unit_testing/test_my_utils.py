import random
import unittest

import my_utils


class TestMyUtils(unittest.TestCase):
    def test_get_column(self):
        # Test case for get_column function
        self.assertEqual(
            my_utils.get_column(
                'test_data.csv',
                0,
                'USA',
                1
            ),
            [100, 200, 300]
        )

    def test_get_column_empty(self):
        # Test case for get_column function with no matching country
        self.assertEqual(
            my_utils.get_column(
                'test_data.csv',
                0,
                'Canada',
                1
            ),
            []
        )

    def test_get_column_random(self):
        # Test case for get_column function with random values
        country = 'USA'
        country_column = 0
        result_column = 1
        expected_results = [
            random.randint(1, 100)
            for _ in range(5)
        ]

        # Create a temporary CSV file with random data
        with open('temp_test_data.csv', 'w') as file:
            file.write('Country,Fires\n')

            for value in expected_results:
                file.write(f'{country},{value}\n')

        self.assertEqual(
            my_utils.get_column(
                'temp_test_data.csv',
                country_column,
                country,
                result_column
            ),
            expected_results
        )

    def test_find_mean(self):
        # Test case for find_mean function
        self.assertAlmostEqual(
            my_utils.find_mean([100, 200, 300]),
            200.0
        )

    def test_find_mean_empty(self):
        # Test empty list case
        self.assertIsNone(
            my_utils.find_mean([])
        )

    def test_find_mean_random(self):
        # Test case for find_mean function with random values
        values = [
            random.randint(1, 100)
            for _ in range(10)
        ]

        self.assertAlmostEqual(
            my_utils.find_mean(values),
            sum(values) / len(values)
        )

    def test_find_median(self):
        # Test case for find_median function
        self.assertAlmostEqual(
            my_utils.find_median([100, 200, 300]),
            200.0
        )

    def test_find_median_empty(self):
        # Test empty list case
        self.assertIsNone(
            my_utils.find_median([])
        )

    def test_find_median_random(self):
        # Test case for find_median function with random values
        values = [
            random.randint(1, 100)
            for _ in range(10)
        ]

        sorted_values = sorted(values)
        mid_index = len(sorted_values) // 2

        if len(sorted_values) % 2 == 0:
            expected_median = (
                sorted_values[mid_index - 1]
                + sorted_values[mid_index]
            ) / 2
        else:
            expected_median = sorted_values[mid_index]

        self.assertAlmostEqual(
            my_utils.find_median(values),
            expected_median
        )

    def test_find_standard_deviation(self):
        # Test case for find_standard_deviation function
        self.assertAlmostEqual(
            my_utils.find_standard_deviation(
                [100, 200, 300]
            ),
            81.65,
            places=2
        )

    def test_find_standard_deviation_empty(self):
        # Test empty list case
        self.assertIsNone(
            my_utils.find_standard_deviation([])
        )

    def test_find_standard_deviation_random(self):
        # Test case for find_standard_deviation with random values
        values = [
            random.randint(1, 100)
            for _ in range(10)
        ]

        mean = sum(values) / len(values)

        variance = (
            sum(
                (value - mean) ** 2
                for value in values
            )
            / len(values)
        )

        expected_std_dev = variance ** 0.5

        self.assertAlmostEqual(
            my_utils.find_standard_deviation(values),
            expected_std_dev
        )


if __name__ == '__main__':
    unittest.main()