# Q4: How many employees in the police department?
import helper
data = helper.read_salaries()

police = helper.get_column(data, 3) # #assign variable name to look in job title column
count_police = helper.count(police, 'POLICE') #count the # of police
print(count_police)
