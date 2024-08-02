dan = int(input("단 입력 : "))

while  True:
	if dan ==0:
		break
	for j in range(9):
		print("{} * {} = {}".format(dan,j+1,((dan)*(j+1))))
	print()
	dan = int(input("단입력 : "))
