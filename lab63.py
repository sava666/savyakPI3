#python3
# coding=utf-8
import sys
import math
import random

sumall = int(input('Enter sum what you wont (UAH) '))
sumget = int(input('Enter sum what you have (UAH) '))
proc = float(input('Enter rate what you have (%)  '))
proc = (proc/100)

def banc(sumall, sumget, proc):
	year=0
	while sumall >= sumget :
		sumget = sumget+sumget*proc
		year=year + 1 
	return year;
	
print('You need to wait for ' + str(banc(sumall, sumget, proc)) + ' years')