#python3
# coding=utf-8
import sys
import math
import random

year = int(input('Enter number of years you want to wait (years) '))
sumget = int(input('Enter sum what you have (UAH) '))
proc = float(input('Enter rate what you want (%)  '))
proc = (proc/100)

def banc(sumget, proc, year):
	count = 0
	while year > count :
		sumget = sumget+sumget*proc
		count=count + 1
	sumall= round (sumget,2)
	return sumall;

print('You will have ' + str(banc(sumget, proc, year)) + ' UAH')

