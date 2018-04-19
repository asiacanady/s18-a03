# Q7: How common is the most common last name? Which is it?
import helper
data = helper.read_salaries()


names = helper.get_column(data, 1)   # get first names
counts = helper.counts(names)         # count them
print(helper.dict_max_value(counts)) # print maximum

last_names = helper.get_column(data, 0) #get last names
counts_last = helper.counts(last_names) #count last names
print(helper.dict_max_value(counts_last)) #print maximum
