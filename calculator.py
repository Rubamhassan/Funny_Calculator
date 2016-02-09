"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
	op_str = raw_input('>')
	op_list = op_str.split(' ')
	if op_list[0]=='+':
		print add(float(op_list[1]),float(op_list[2]))
	elif op_list[0]=='-':
		print subtract(float(op_list[1]),float(op_list[2]))
	elif op_list[0]=='*':
		print multiply(float(op_list[1]),float(op_list[2]))
	elif op_list[0]=='/':
		if float(op_list[2]) == 0:
			print 'Error: Division by zero! Try Again'
		else:
			print divide(float(op_list[1]),float(op_list[2]))
	elif op_list[0]=='square':
		print square(float(op_list[1]))
	elif op_list[0]=='cube':
		print cube(float(op_list[1]))
	elif op_list[0]=='pow':
		print power(float(op_list[1]),float(op_list[2]))
	elif op_list[0]=='mod':
		print mod(float(op_list[1]),float(op_list[2]))
	elif op_list[0]=='q':
		break
	else:
		print "I don't understand"
