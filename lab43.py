# coding=utf-8
import sys
import math
import decimal

money = float(input('input youre money\n'))
#podat 19.5%

cash = decimal.Decimal(money)*decimal.Decimal('0.195')
cash=str(round(cash,2))

print('YOU NEED TO PAYYY!! ' + cash + '$ FROM YOURE SELARY')




