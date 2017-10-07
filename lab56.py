#python3
# coding=utf-8
import sys
import math
import random
a = float(input('Enter side a of triangle '))
b = float(input('Enter side b of triangle '))
c = float(input('Enter side c of triangle '))

if (((a+b)>c) and ((b+c)>a) and ((c+a)>b)):
	print('Youre triangle exist')
else:
	print('Youre triangle doesnt exist')
