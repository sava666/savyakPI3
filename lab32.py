# coding=utf-8
import sys
question = 'what do you want?\n1.Convert celsius into 	fahrenheit\n2.Convert fahrenheit into celsius\n\n'
choise = int(input(question))
if choise==1:
	#print('you chose 1')
	temp = float(input('write temperature in fahrenheit\n'))
	cTemp = (temp*1.8)+32
	print('temperature in celsius '+ str(cTemp))
elif choise==2:
	#print('you chose not 2')
	temp = float(input('write temperature in celsius\n'))
	cTemp = (temp-32)/1.8
	print('temperature in fahrenheit '+ str(cTemp))
else:
	print('wrong number try again')
	

