# coding=utf-8
import sys
import math
import decimal

a = float(input('input a\n'))
b = float(input('input b\n'))
c = float(input('input c\n'))

f = (1/(c*math.sqrt(2*math.pi))) * math.exp(-((math.pow(a-b,2)/(2*math.pow(c,2)))))
print(f)

