# Q2: How many full time employees are there?
import helper
data = helper.read_salaries()

full_time = helper.get_column(data, 4) #assign variable name to look in 'position type' column
count_fulltime = helper.count(full_time, 'F') #count the specific number of full time employees
print(count_fulltime)
