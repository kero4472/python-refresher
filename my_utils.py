def get_column(file_name, query_column, query_value, result_column=1):

    results = []

    try:
        with open(file_name, 'r') as file:

            for line in file:

                columns = line.strip().split(',')

                if len(columns) <= max(query_column, result_column):
                    continue

                if columns[query_column] == query_value:

                    try:
                        value = int(float(columns[result_column]))
                        results.append(value)

                    except ValueError:
                        print(
                            'Could not convert '
                            + columns[result_column]
                            + ' to an integer'
                        )

    except FileNotFoundError:
        print('Could not find ' + file_name)

    except PermissionError:
        print('Could not open ' + file_name)

    return results