year = int(input("년도 입력 : "))

if year%4==0 and year%100!=0 or year%400==0:
	print("윤년(leap year)입니다.")
else:
	print("평년(common year)입니다.")
