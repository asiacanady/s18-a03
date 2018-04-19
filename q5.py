# Q5: How many detectives?
import helper
data = helper.read_salaries()

detectives_list = helper.get_column(data, 2) # #assign variable name to look in Job Title column
detectives_count = helper.count(detectives_list, "POLICE OFFICER (ASSIGNED AS DETECTIVE)") #count the number of detectives
print(detectives_count)
