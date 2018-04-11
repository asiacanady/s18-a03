# Assignment 3: Data Manipulation with Python
In this assignment we will revisit the city of Chicago's employee salary file using Python. You may only use built-in python functions in this assignment (so no `pandas` or `numpy` if you're already familiar with those).

## A: CSV parser
First you will parse the `salaries.csv` using a function called `read_salaries` that takes the filename as a parameter. So your function should have a signature like so:
```python
def read_salaries(filename):
    ...
```

Put your function in a file called `helper.py` so that it will be accessible in the rest of the problem set through a `helper` module.

Your parser should do the following:
 1. Read each line, ignoring/removing the first (header) line
 2. Split each line on the ',' and return a nested list where each element is itself a list of fields.
 3. Note that this will split the first field as well because there is a comma separating last and first name. This is fine. However, there will be a double quote at the beginning of the last name field and the end of the first name field. Remove these characters. Also remove extra white space from the beginning of the first name field.
 4. The first name may have a middle name. Remove it by splitting on ' ' and keeping the first element.
 5. Convert salaries, when present, to number by first removing the dollar sign and then using hte type conversion function `float`.
 
## B: Additional helper functions
In the `helper.py` function also implement the following functions to be used in part C below.

 1. `get_column(data, column_index)`: Given a 2d list `data` and an integer `column_index` (e.g. 0 for last name, 3 for department), return a (one dimensional) list of values for that column (4 points).
 2. `count(values)`: Given a 1d list `values` (e.g. the result of `get_column`), return a dictionary of value-count pairs (4 points).
 3. `dict_max_value(d)`: Given a dictionary `d` with numeric values, return a list `[key, value]` of two elements, where `key` is the the key in `d` with the largest value, and `value` is it's value (4 points).
 4. `mean(numbers)`: given a list of numbers use the built-in functions `sum` and `len` to return their mean
 5. `percentile(numbers, p)`: given a list of numbers expand the example from class to calculate the `p`-th percentile, i.e. the `p*len(numbers)` element in the sorted list.
 
 If `p*len(numbers)` is not an integer, you should take the average between the adjacent elements in the sorted lists.. For example, when `p=.5` and len(numbers) is 6, `percentile(numbers, p)` should return the average between the 3rd and 4th items in the sorted list. 

## C: Analysis of salaries
Repeat the analysis from assignment 1 using the `helper` module you developed in parts A and B.

1. How many employees does the city have (4 points)?
2. How many full time employees (4 points)?
3. How many part-time employees (4 points)?
4. How many employees in the police department (4 points)?
5. How many detectives (4 points)?
6. What is the largest department (8 points)?

Do the following additional analysis:

7. What is the most common first name? (4 points)
7. What are the minimum, 25th percentile, mean, median, 75th percentile, and maximum salaries? In addition to the `percentile` and `mean` helpers you wrote, you may use the built-in python functions `min` and `max`.
