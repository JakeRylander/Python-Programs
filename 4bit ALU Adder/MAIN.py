#--------------------------------------------
#Author Information
#CCOM 3030 - UPRRP 
#John G. Wilson Negroni (801-14-8684) 
#4Bit Integer Adder and Subtractor
#Ver. 1.0
#Python 2.7.7
#--------------------------------------------
#Lists
list1 = []
list2 = []
#--------------------------------------------
#Imports
from alu4bit import *
import time
import sys
#--------------------------------------------
#Variables
state = 0
#--------------------------------------------
#Functions
def numcheck(check):
	while True:
		input = raw_input("Enter an Integer: ")
		try:
			input = int(input)
		except ValueError:
			print "Invalid Character, Please input a Valid one."        
		else:
			input = int(input)
			if input > 7:
				print "The Number is too big."
			elif input < -8:
				print "The Number is too small."                
			else:
				binary(input)
				break
def binary(parameter):
	while True:
		if state == 1:
			x = list1
			break
		elif state == 2:
			x = list2
			break
	if parameter < 0:
		d = 8 + parameter
		while d != 0:
			modulo = d % 2
			d = d/2
			x.append(modulo)
		while len(x) < 3:
			x.append(0)
		x.append(1)
		if len(x) == 5:
			x.reverse()
			x.remove(0)
			x.reverse()
		x.reverse()
		print x
		x.reverse()
	else:
		d = parameter
		while d != 0:
			modulo = d % 2
			d = d/2
			x.append(modulo)
		while len(x) < 4:
			x.append(0)
		x.reverse()
		print x
		x.reverse()
def baseten(number):
        exponent = 3
        result = 0
        number = flipList(number)
        for i in number:
            if exponent == 3:
                if i == 1:
                    result += number[i] * (2**exponent) * -1
                else:
                    result += i * (2**exponent)
            else:
                result += i * (2**exponent)
            exponent -= 1
        return result
#--------------------------------------------
#Actual Program
print "-------------------------------------------------"
print "Binary Calculator 4bit Calculator (-8 to 7 range)"
print "-------------------------------------------------"
print ""
while True:
	state = 1
	numcheck(state)
	state = 2
	numcheck(state)
	while True:
		input = raw_input ("Enter 0 for Addition or 1 for Subtraction: ")
		try:
			input = int(input)
		except ValueError:
			print "Invalid Character, Please input a Valid one."        
		else:
			if input > 1 or input < 0:
				print "Invalid Number Operator, Please input a Valid one."
			else:
				break
	while True:
		op = int(input)            
		res, over = alu4bit(list1, list2, op)
		if over:
			print "Overflow Error"
		print "The result is: ", baseten(res)
		res.reverse()
		print res
		print "Do you want to Quit? Write 'Yes' to quit, or nothing/anything else to continue: "	
		user_input = raw_input()
		user_input = user_input.lower()
		if user_input != "yes":
			list1 = []
			list2 = []
			state = 0
			print ""
			break
		else:
			print "Thanks for using, program quitting now."
			time.sleep (3)
			sys.exit ()