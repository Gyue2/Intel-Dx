def factorialNum(num):
    if num == 1:
        return 1
    else:
        return num * factorialNum(num - 1)

inputData = int(input('0 보다 큰 숫자 입력 : '))
result = factorialNum(inputData)
print(inputData,'팩토리얼 = ',result)