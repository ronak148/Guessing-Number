
import random

print("Let's Play")
a=int(raw_input("Start Number:"))
b=int(raw_input("Last Number:"))


x = random.randint(a,b)
print(x)


y=int(raw_input("Enter Number:"))
print(y)
atp=3
if (y ==x):
	print("congratulation")
if(y!=x):
	print ('Sorry Try again you have {} left'.format(atp-1))

y=int(raw_input("Enter Number:"))
print(y)

if(y!=x):
	print ('Sorry Try again you have {} left'.format(atp-2))
	y=int(raw_input("Enter Number:"))
print(y)

if(y!=x):
	print ('Sorry Game Over')







