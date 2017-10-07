#python3
# coding=utf-8
import sys
import math
import random
choises=['paper','rock','scissors']
ch = int(input("Enter youre choise:\n1.paper\n2.rock\n3.scissors\n"))
ch2 =random.randint(1,3)

if((ch==1 and ch2==2) or (ch==2 and ch2==3) or (ch==3 and ch2==1)):
	print('you win \nyou chose '+choises[ch-1]+'\ncomputer chose '+choises[ch2-1])
elif((ch2==1 and ch==2) or (ch2==2 and ch==3) or (ch2==3 and ch==1)):
	print('you lose\nyou chose '+choises[ch-1]+'\ncomputer chose '+choises[ch2-1])
else:
	print('its a draw\nyou chose '+choises[ch-1]+'\ncomputer chose '+choises[ch2-1])


