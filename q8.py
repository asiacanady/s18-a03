# Q8: What are the minimum, mean, median, and maximum salaries?
import helper

data = helper.read_salaries()

salaries = []
# TODO: get non-empty salaries from data

print('Minimum:', min(salaries))
print('Mean:', helper.mean(salaries))
print('Median:', helper.median(salaries))
print('Maximum:', max(salaries))
