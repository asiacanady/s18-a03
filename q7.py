# Q7: How common is the most common last name? Which is it?
import helper

data = helper.read_salaries()
names = helper.get_column(data, 1)
counts = helper.counts(names)

print(helper.dict_max_value(counts))
