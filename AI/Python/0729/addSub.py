import random

x = random.randint(1,100)
y = random.randint(1,100)

op = random.randint(1,4)

if op==1:
	answer = int(input(f"{x} + {y} = "))
	flag = (answer == (x + y))

elif op==2:
	answer = int(input(f"{x} * {y} = "))
	flag = (answer == (x * y))

elif op==3:
	if x > y:
		answer = float(input(f"{x} / {y} = "))
		flag = (answer == round((x/y),2))
	else:
		answer = float(input(f"{y} / {x} = "))
		flag = (answer == round((y/x),2))
else:
	if x > y:
		answer = int(input(f"{x} - {y} = "))
		flag = (answer == (x - y))
	else:
		answer = int(input(f"{y} - {x} = "))
		flag = (answer == (y - x))

print(flag)
