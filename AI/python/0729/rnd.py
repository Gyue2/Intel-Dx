import random

x = random.randint(1,100)
y = random.randint(1,100)

answer = int(input(f"{x} + {y} = "))

correct = (answer == (x+y))
if correct:
	print("정답입니다.")
else:
	print("다시 하세요.")
