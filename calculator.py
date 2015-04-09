"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic1 import *


# Your code goes here



def calculator():
    while True:
        print "Please enter your calculations in prefix mode with spaces as separation between items."
        print "Print q to quit."
        user_calculating = raw_input("What would you like to calculate?")
        tokens = user_calculating.split(" ") # ["pow", "3", "5"]
        if tokens[0] == "q":
            break
        elif tokens[0] == "add":
            return arithmetic1.add()


if __name__ == "__main__":
    calculator()


