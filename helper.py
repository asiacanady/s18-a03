#helper.py

def read_salaries():#parsed filed and split each line on ',' where each element is itslef a list of fields
    file = open('salaries.csv')
    lines = [] #create list
    for line in file:
        fields = line[:-1].split(',')
        #remove the dollar signs
        fields[7] = fields[7][1:] #the 1: removes the dollar sign from salary and keeps the rest of the value
        fields[0] = fields[0][1:] #removes quotes from last names
        fields[1] = fields[1][2:] #removes spaces from in front of first name
        clean_first = fields[1].split(" ") #splits the first name w/ empty space
        fields[1] = clean_first
        lines.append(fields[0][1])

    return lines #return salaries with everything after the first row

data = read_salaries() #parsed and cleaned data

# A.2 Given a 2d list data and an integer column_index
# return a 1d list of values for that column.
def get_column(data, column_index): #define the funtion
    column = []
    for row in data: #Look for the row in the data
        column.append(row[column_index]) #append the row nested in the column index
    return column #return the column

# A.3: Given a 1d list of `values` (e.g. the result of get_column),
# return the number of elements that are equal to `search_value`.
def count(values, search_values):
    count = 0 #start count from the least possible value
    for lines in values:
        if lines == search_values: #set up condition
            count += 1 #add one everytime lines = search_values
    return count

# A.4: Given a 1d list values (e.g. the result of get_column),
# return a dictionary of value-count pairs.
def counts(values):
    results = {} #create dictionary
    for value in values:
        if value not in results: #search for values not on results
            results[value] = 1
        else:
            results[value] += 1 #adds another value to the variables value
    return results

# A.5: Given a dictionary d with numeric values, return a list [key, value] of two elements,
# where key is the the key in d with the largest value, and value is it's value.
def dict_max_value(d):
    d.values()
    search = max(d.values()) #search for the key with the max value
    for key in d: #iterate over the dictionary
        if d[key] == search: #lookup the value for each key in the loop
            print(key, ":", d[key])
    return [None, 0]

# A.6: Given a list of numbers use the built-in functions sum and len to return their mean.
def mean(numbers):
    sum_output = sum(numbers)
    len_output = len(numbers)
    mean_output = sum_output / len_output
    return mean_output

# A.7: Given a list of numbers calculate the median.
def median(numbers):
    numbers_sorted = sort(numbers) #sort the variables to find median
    median=[(numbers_sorted/2)] #divide sorted variables by 2 to find median
    return median
