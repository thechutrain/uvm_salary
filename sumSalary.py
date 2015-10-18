__author__ = 'alanchu'
#  This function takes in the master list of the employee salary as a Decimal
#  Object and gets the sum


def sumSalary(employee_list):
    sumSalary = 0
    for e in employee_list:
        if (e[2] == None):
            pass
        else:
            sumSalary += e[2]
    return sumSalary

