__author__ = 'alanchu'
#  This python file will call multiple functions that I am working on, and
#  test to see that they are working.  This file will also be a sort of coding playground

################# IMPORT #######################
from open_cleanfile import open_cleanfile  # imports open_cleanfile function
from count_positions import count_positions  # imports open_cleanfile function
from decimal import Decimal
import pprint
import operator

################# TESTING GROUND ##############
clean_employee_list = open_cleanfile("uvmSalary15.csv")
sorted_position_list = count_positions(clean_employee_list, "d")  #returns a list of tuples!!

# pprint.pprint(sorted_position_list[1])

# # sort the clean_employee_list by position?
# sorted_employee_list = sorted(clean_employee_list, key=operator.itemgetter(1), reverse=True)
# pprint.pprint(sorted_position_list)

position_salary_distribution_list = []
for i in range(2): #  gets first 10 positions from sorted_position_list[]
    temp_array = []
    # DEBUGGING & DATA TYPE
    # print type(sorted_position_list[i][0]) # str
    # print type(sorted_position_list[i][1]) # int
    # break

    temp_array.append(sorted_position_list[i][0])  # appends the position
    temp_array.append(sorted_position_list[i][1])  # appends the count of that position
    #temp_array.append(sum)
    position_salary_distribution_list.append(temp_array)
    # DEBUGGING & DATA TYPE
    # pprint.pprint(sorted_position_list[i])
    # print type(sorted_position_list[1])
    # break

#testing my list:
pprint.pprint(position_salary_distribution_list)
print position_salary_distribution_list
# print position_salary_distribution_list[0][0]   # should be associate professor
# print position_salary_distribution_list[1][0]
# value = Decimal(0)
# print value
# print type(value)