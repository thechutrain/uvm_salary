__author__ = 'alanchu'
#  This python file will call multiple functions that I am working on, and
#  test to see that they are working.  This file will also be a sort of coding playground

################# IMPORT #######################
from open_cleanfile import open_cleanfile  # imports open_cleanfile function
from count_positions import count_positions  # imports open_cleanfile function

################# TESTING GROUND ##############
clean_employee_list = open_cleanfile("uvmSalary15.csv")
sorted_position_list = count_positions(clean_employee_list, "d")