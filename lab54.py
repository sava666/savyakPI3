#python3
# coding=utf-8
import sys
import math
import random
a = int(input('Enter cof a '))
b = int(input('Enter cof b '))
c = int(input('Enter cof c '))

#ax^2+bx+c=0
D = (b*b)-(4*a*c)

if D>=0:
	x1=(-b + math.sqrt(D))/2*a
	x2=(-b - math.sqrt(D))/2*a
	print('x1 = ' + str(x1))
	print('x2 = ' + str(x2))
else:
	print('Youre equation has no solutions')
