__author__ = 'alanchu'
#
# This function opens new file and cleans the
# data and returns a list containing employee name, salaries, position

############################# DEBUGGING   ###################################
# import os
# print "hello world"
# print os.getcwd()

############################# IMPORT #############################
import pprint

def openfile(filename):
    try:
        f = open(filenmae, 'rU')
    except IOError:
        