n = int(input("양의 정수 입력 : "))
fact = 1

for i in range(1,n+1):
	fact *= i

print("{}! = {}".format(n,fact))

