# Assignment 3: Data Manipulation with Python
In this assignment we will revisit the city of Chicago's employee salary file using Python. You may only use built-in python functions in this assignment (so no `pandas` or `numpy` if you're already familiar with those).

## A: Helpers
Write the following functions in order to complete part B. Put them in a file called `helper.py` in the assignment's directory so that they will be accessible in the rest of the problem set in python through a `helper` module. When you accept the assignment you will find a template `helper.py` file with function signatures and some hints.

 1. `read_salaries(filename)`: Parse the included `salaries.csv` file. Your parser should split each line on ',' and return a nested list where each element is itself a list of fields. Additoinally you should ignore/remove the first (header) line. (4 points)
 2. `get_column(data, column_index)`: Given a 2d list `data` and an integer `column_index` (e.g. 0 for last name, 3 for department), return a (one dimensional) list of values for that column. (4 points)
 3. `count(values)`: Given a 1d list `values` (e.g. the result of `get_column`), return a dictionary of value-count pairs. (4 points)
 4. `dict_max_value(d)`: Given a dictionary `d` with numeric values, return a list `[key, value]` of two elements, where `key` is the the key in `d` with the largest value, and `value` is it's value. (4 points)
 5. `mean(numbers)`: given a list of numbers use the built-in functions `sum` and `len` to return their mean. (4 points)
 6. `median(numbers)`: given a list of numbers calculat the median. (4 points)

    Your function should *not* modify `numbers` inplace. Expand the example from class to work when `len(numbers)` is even using the following logic:
 
    If `p*len(numbers)` is not an integer, take the average between the adjacent elements in the sorted list. For example, when `p=.5` and len(numbers) is 6, `percentile(numbers, p)` should return the average between the 3rd and 4th items in the sorted list.
    
    You can check that your function is working at the interactive interpretter:
    
    ```python
    >>> import helper
    >>> helper.median([5,3,1,2,4])
    3
    >>> helper.median([4,1,2,3])
    2.5
    ```

## B: Analysis of salaries
Repeat the analysis from assignment 1 using the `helper` module you developed in part A. Each question will 

1. How many employees does the city have (4 points)?
2. How many full time employees (4 points)?
3. How many part-time employees (4 points)?
4. How many employees in the police department (4 points)?
5. How many detectives (4 points)?
6. What is the largest department (4 points)?

Do the following additional analysis:

7. What is the most common first name? (8 points)
Note that when you split on ',' in your parser, you separated the employee first and last and first names. However, there will be a double quote at the beginning of the last name field and the end of the first name field. So update `helper.read_salaries` to:
    - Remove these characters.
    - Also remove extra white space from the beginning of the first name field.
    - Also the first name may have a middle name. Remove it by splitting on ' ' and keeping the first element.

8. What are the minimum, 25th percentile, mean, median, 75th percentile, and maximum salaries? (8 points)

In addition to the `percentile` and `mean` helpers you wrote, you may use the built-in python functions `min` and `max`. You'll need to update `helper.read_salaries` to convert salaries, when present, to a number. Hint: first removing the dollar sign and then using the type conversion function `float`. Also be sure to ignore missing salaries (for wage workers) in your calculations here.
