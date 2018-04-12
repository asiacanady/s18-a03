# Assignment 3: Data Manipulation with Python
In this assignment we will revisit the city of Chicago's employee salary file using Python. You may only use built-in python functions in this assignment (so no `pandas` or `numpy` if you're already familiar with those).

## Part A: Helpers
Write the following 7 functions. You will use them later to complete part B. Put these 7 Part A functions in a file called `helper.py` in the assignment's directory so that they will be accessible in the rest of the problem set in python through a `helper` module. When you accept the assignment you will find a template `helper.py` file with function signatures and some hints.

 1. `read_salaries()`: Parse the included `salaries.csv` file. Your parser should split each line on ',' and return a nested list where each element is itself a list of fields. Additionally you should ignore/remove the first (header) line. (4 points)
 2. `get_column(data, column_index)`: Given a 2d list `data` and an integer `column_index` (e.g. 0 for last name, 3 for department), return a (one dimensional) list of values for that column. (4 points)
 3. `count(values, search_value)`: Given a 1d list of `values` (e.g. the result of `get_column`), return the number of elements that are equal to `search_value`.
 4. `counts(values)`: Given a 1d list `values` (e.g. the result of `get_column`), return a dictionary of value-count pairs. (4 points)
 5. `dict_max_value(d)`: Given a dictionary `d` with numeric values, return a list `[key, value]` of two elements, where `key` is the the key in `d` with the largest value, and `value` is it's value. (4 points)
 6. `mean(numbers)`: given a list of numbers use the built-in functions `sum` and `len` to return their mean. (4 points)
 7. `median(numbers)`: given a list of numbers calculate the median. (4 points)

    Your median function should *not* modify `numbers` inplace. Expand the example from class to work when `len(numbers)` is even using the following logic: If `len(numbers)` is odd, take the middle element in the sorted list. If 'len(numbers)' is even, there will be two adjacent "middle" elements in the sorted list. Take the average between them. You can check that your median function is working using the interactive interpretter:
    
    ```python
    >>> import helper
    >>> helper.median([5,3,1,2,4])
    3
    >>> helper.median([4,1,2,3])
    2.5 # this is (2+3)/2
    ```

## B: Analysis of salaries
Repeat the analysis from assignment 1 using the `helper` module you developed in part A. Put your solution to B.1 in `q1.py`, B.2 in `q2.py` and so on. Each question has a template python script to get you started.

B.1: How many employees does the city have (4 points)?

B.2: How many full time employees (4 points)? Hint: use `get_column()` and `count()` above.

B.3: How many part-time employees (4 points)?

B.4: How many employees in the police department (4 points)?

B.5: How many detectives (4 points)?

B.6: What is the largest department? Note that `q6.py` is already written for you and will work if you implemented the helper functions correctly. (0 ponts)

Do the following additional analysis:

B.7: What is the most common first name? Again, `q7.py` is written for you. What you'll need to do is modify the parser: (4 points)

Note that when you split on ',' in your parser, you separated the employee first and last and first names. However, there will be a double quote at the beginning of the last name field and the end of the first name field. So update `helper.read_salaries` to:
    - Remove these characters.
    - Also remove extra white space from the beginning of the first name field.
    - Also the first name may have a middle name. Remove it by splitting on ' ' and keeping the first element.

B.8: What are the minimum, mean, median, and maximum salaries? (4 points)

`q8.py` is partially written for you. You'll need to get the salaries from the data, ignoring/removing those that are empty (wage workers). You'll also need to update `helper.read_salaries` to convert salaries, when present, to a number. Hint: first remove the dollar sign and then use the type conversion function `float`.
