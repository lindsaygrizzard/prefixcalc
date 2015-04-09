"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
print "Please enter your calculations in prefix mode with spaces as separation between items."
print "Print q to quit."
print "Type squ to squaring your number, cube to cube, pow, mod, (+ - * / as usual)"


def calculator():
    while True:
        user_calculating = raw_input("What would you like to calculate? ")
        tokens = user_calculating.split(" ") # ["pow", "3", "5"]
        
        if tokens[0] == "q":
            break
        elif tokens[1:] != int():
            print "Please reread the instructions and use this only for number calculations!"  
        elif tokens[0] == "+":
            print add(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "-":
            print subtract(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "*":
            print multiply(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "/":
            print divide(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "squ":
            print square(int(tokens[1]))
        elif tokens[0] == "cube":
            print cube(int(tokens[1]))
        elif tokens[0] == "pow":
            print power(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "mod":
            print mod(int(tokens[1]), int(tokens[2]))
        else:
            print "Please reread the instructions and use this only for number calculations!"


if __name__ == "__main__":
    calculator()
