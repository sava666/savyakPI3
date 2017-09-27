# coding=utf-8
import sys
import math
import decimal



a =float(input('input a\n'))
b=float(input('input b (b != 0)\n'))

x = math.sqrt(a*b)/(math.exp(a) * b)+a*math.exp((2*a)/b)

print (x)

