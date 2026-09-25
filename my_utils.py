def get_column(file_name, query_column, query_value, result_column=1):
    """
    Return integer values from a selected column of a CSV file.

    The function reads the CSV file one line at a time and checks whether
    the value in query_column matches query_value. If a match is found,
    the value from result_column is converted to an integer and added to
    the results list.

    Returns:
        A list of integers from rows that match the query value.
    """

    # Create an empty list to store matching values
    results = []

    try:
        # Open the CSV file for reading
        with open(file_name, 'r') as file:

            # Read the file one line at a time
            for line in file:

                # Remove whitespace and split the row into columns
                columns = line.strip().split(',')

                # Skip rows that do not contain the requested columns
                if len(columns) <= max(query_column, result_column):
                    continue

                # Check if the query column matches the requested value
                if columns[query_column] == query_value:

                    try:
                        # Convert the result value to an integer
                        value = int(float(columns[result_column]))

                        # Add the converted value to the results list
                        results.append(value)

                    except ValueError:
                        # Handle values that cannot be converted to an integer
                        print(
                            'Could not convert '
                            + columns[result_column]
                            + ' to an integer'
                        )

    except FileNotFoundError:
        # Handle the case where the file does not exist
        print('Could not find ' + file_name)

    except PermissionError:
        # Handle the case where the file cannot be opened
        print('Could not open ' + file_name)

    # Return all matching integer values
    return results


def find_mean(values):
    """
    Return the mean of a list of integers.

    The function calculates the mean by summing all values and dividing
    by the number of values. If the list is empty, it returns None.

    Returns:
        The mean of the list as a float, or None if the list is empty.
    """

    # Check if the list is empty
    if len(values) == 0:
        return None

    # Calculate the mean
    total = sum(values)
    count = len(values)
    mean = total / count

    return mean


def find_median(values):
    """
    Return the median of a list of integers.

    The function calculates the median by sorting the list and finding
    the middle value. If the list is empty, it returns None.

    Returns:
        The median of the list as a float, or None if the list is empty.
    """

    # Check if the list is empty
    if len(values) == 0:
        return None

    # Sort the values to find the median
    sorted_values = sorted(values)
    count = len(sorted_values)
    mid_index = count // 2

    # Calculate median based on even or odd number of values
    if count % 2 == 0:
        median = (sorted_values[mid_index - 1] + sorted_values[mid_index]) / 2
    else:
        median = sorted_values[mid_index]

    return median


def find_standard_deviation(values):
    """
    Return the standard deviation of a list of integers.

    The function calculates the standard deviation using the formula:
    sqrt(sum((x - mean)^2) / n), where n is the number of values.
    If the list is empty, it returns None.

    Returns:
        The standard deviation of the list as a float, or None if the list is empty.
    """

    # Check if the list is empty
    if len(values) == 0:
        return None

    # Calculate the mean
    mean = find_mean(values)

    # Calculate the variance
    variance = sum((x - mean) ** 2 for x in values) / len(values)

    # Calculate the standard deviation
    std_dev = variance ** 0.5

    return std_dev