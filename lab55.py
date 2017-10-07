#python3
# coding=utf-8
import sys
import math
import random
num = int(input('Enter number (number > 0) '))
if num > 0:
	while num%2==0 or num%3==0 or num%5==0 or num%7==0:

		if num==2 or num==3 or num==5 or num==7 :
			print(str(num) + ' is prime number') 
			break
		print(str(num) + ' isnt prime number')
		break
	else:
		print(str(num) + ' is prime number')
		#break
		
else:
	print('number isnt >0( try again')

