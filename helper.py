# A.1: Parse the included salaries.csv file.
# Your parser should split each line on ',' and return a nested list 
# where each element is itself a list of fields. 
# Additionally you should ignore/remove the first (header) line.
def read_salaries():
    salaries = [[]]

# A.2: Given a 2d list data and an integer column_index 
# return a 1d list of values for that column.
def get_column(data, column_index):
    return []

# A.3: Given a 1d list of `values` (e.g. the result of get_column), 
# return the number of elements that are equal to `search_value`.
def count(values, search_values):
    return 0

# A.4: Given a 1d list values (e.g. the result of get_column),
# return a dictionary of value-count pairs.
def counts(values):
    return {}

# A.5: Given a dictionary d with numeric values, return a list [key, value] of two elements,
# where key is the the key in d with the largest value, and value is it's value. 
def dict_max_value(d):
    return [None, 0]

# A.6: Given a list of numbers use the built-in functions sum and len to return their mean.
def mean(numbers):
    return 0.0

# A.7: Given a list of numbers calculate the median.
def median(numbers):
    return 0.0
