# Q3: How many part-time employees are there?
import helper #import module
data = helper.read_salaries()

part_time = helper.get_column(data, 4)  #assign variable name to look in position type
count_parttime = helper.count(part_time, 'P') #count the specific type of part-time employees
print(count_parttime)
