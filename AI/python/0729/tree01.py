loop = int(input("층의 갯수 입력 : "))

for n1 in range(loop):
	for n2 in range(loop-n1-1):
		print(" ",end="")

	for n3 in range((n1+1)*2-1):
		print("*",end="")

	print()

