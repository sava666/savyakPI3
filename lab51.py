#python3
# coding=utf-8
import sys
import math

number = int(input("Enter youre number >0 "))
if number>0:
	#print(number)
	a = math.log(number,2)
	b = int(math.log(number,2))

	if b==a :
		print("This number is degree of number 2")
	else:
		print("THis number isn't degree of number 2")
else:
	print("Write number >0")









