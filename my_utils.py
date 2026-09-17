def get_column(file_name, query_column, query_value, result_column=1):

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