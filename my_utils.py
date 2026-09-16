def get_column(file_name, query_column, query_value, result_column=1):
    results= []
    with open(file_name, 'r') as file:
        for line in file:
            columns = line.strip().split(',')
            if len(columns) <= max(query_column, result_column):
                continue
            if columns[query_column] == query_value:
                results.append(columns[result_column])
    return results