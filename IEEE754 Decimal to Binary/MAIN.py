#--------------------------------------------
#Author Information
#CCOM 3030 - UPRRP 
#John G. Wilson Negroni (801-14-8684) 
#IEEE754 Decimal to Binary Converter (16,32,64)
#Ver. 1.0
#Python 2.7.7
#--------------------------------------------
#Lists
list = []
listdecimal = []
listexp = []
listint = []
listmantisa = []
#--------------------------------------------
#Imports
import time
import sys
import math
#--------------------------------------------
#Variables
mantisa = 0
exp = 0
bias = 0
sign = 0
num = 0
bits = 0
calculation = 0
integer = 0
binarynumber = 0
expcounter = 0
#--------------------------------------------
#Functions
def binary(bits, num, mantisa, exp, bias):
	calculation = num
	calculation = float(calculation)
	if calculation < 0:
		sign = 1
		calculation = calculation * -1
	else: 
		sign = 0
		
	if calculation >= 1:
		integer = math.floor(calculation)
		integer = int(integer)
		decimal = calculation - integer
		while integer != 0:
			residue = integer % 2
			integer = integer/2
			listint.append(residue)
		listint.reverse()
		integer = int(''.join(map(str,listint)))
	else:
		integer = 0
		listint.append(integer)
		decimal = calculation
	listdecimal.append(".")
	for x in range(1, mantisa+10):
		decimal = decimal * 2
		intdecimal = int(decimal)
		listdecimal.append(intdecimal)
		if decimal >= 1:
			decimal -= 1
	decimal = float(''.join(map(str,listdecimal)))
	binarynumber = integer + decimal
	binexp = binarynumber
	
	expcounter = 0
	if integer == 0:
		while binexp < 1:
			binexp = binexp * (10**(1))
			expcounter = expcounter - 1
	else:
		while binexp > 2:
			binexp = binexp * (10**(-1))
			expcounter = expcounter + 1
	expcounter2 = expcounter
	expcounter = expcounter + bias	
	while expcounter != 0:
		residue = expcounter % 2
		expcounter = expcounter/2
		listexp.append(residue)
	while len(listexp) < 5:
		listexp.append (0)
	listexp.reverse()
	expcounter = expcounter2
	listdecimal.remove (".")
	if integer == 0:
		counter = expcounter
		if counter < 0:
			counter = counter * (-1)
		while counter > 0:
			x = 0
			listdecimal.pop(x)
			counter = counter - 1
			x = x + 1
	if integer == 0:
		listmantisa = listdecimal
	else:
		listmantisa = listint + listdecimal
	if integer == 0:
		listexp.pop(0)
		listexp.insert (0,0)
	else:
		listmantisa.pop(0)	
		
	while len(listmantisa) > mantisa:
		listmantisa.pop()
	list = []
	if sign == 1:
		list.append (1)
	else:
		list.append (0)

	list = list + listexp + listmantisa 
	
	num2 = 1	
	valuexp = 0
	for i in listmantisa:
		valuexp = valuexp - 1
		if i == 1:
			num2 = num2 + (2**valuexp)
	if sign == 1:
		num2 = num2 * (-1)
	num2 = num2 * (2**expcounter)
	
	print "Sign: ", sign
	print "Exponent: ", listexp
	print "Mantisa: ", listmantisa
	print "Full Representation: ", list
	print "Original Number: ", num
	print "Represented Number: ", num2
	print "Amount of Error: ", num - num2
#--------------------------------------------
#Actual Program
print "------------------------------------------------------------"
print "IEEE754 Decimal to Binary Converter (16,32 and 64 bit range)"
print "------------------------------------------------------------"
print ""
while True:
	while True:
		num = raw_input("Enter the Number to convert: ")
		try:
			num = float(num)
		except ValueError:
			print "Invalid character, please input a valid character"        
		else:
			break
	while True:
		bits = raw_input("Enter the amount of bits to calculate with (16, 32, 64): ")
		try:
			bits = int(bits)
		except ValueError:
			print "Invalid character, please input a valid character"
		else:
			if bits != 16 and bits != 32 and bits != 64:
				print "Incorrect amount of bits, please input a valid one"
			else:
				if bits == 16:
					if num < (((2**16)/2)-1) and num > (-(2**16)/2):
						mantisa = 10
						exp = 5
						bias = 15
						binary(bits, num, mantisa, exp, bias)
						break
					else:
						print "That number is not workable with those amount of bits" 
						break
				elif bits == 32:
					if num < (((2**32)/2)-1) and num > (-(2**32)/2):
						mantisa = 23
						exp = 8
						bias = 127
						binary(bits, num, mantisa, exp, bias)
						break
					else:
						print "That number is not workable with those amount of bits"
						break
				elif bits == 64:
					if num < (((2**64)/2)-1) and num > (-(2**64)/2):
						mantisa = 52
						exp = 11
						bias = 1023
						binary(bits, num, mantisa, exp, bias)
						break
					else:
						print "That number is not workable with those amount of bits"
						break
	while True:
		print "Do you want to Quit? Write 'Yes' to quit, or nothing/anything else to continue: "	
		user_input = raw_input()
		user_input = user_input.lower()
		if user_input != "yes":
			print ""
			mantisa = 0
			exp = 0
			bias = 0
			sign = 0
			num = 0
			bits = 0
			calculation = 0
			integer = 0
			binarynumber = 0
			expcounter = 0
			list = []
			listdecimal = []
			listexp = []
			listint = []
			listmantisa = []
			break
		else:
			print "Thanks for using, program quitting now."
			time.sleep (3)
			sys.exit ()