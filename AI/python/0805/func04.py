import os

def add():
    print('덧셈 결과 :',inputNum1 + inputNum2)

def sub():
    print('뺄셈 결과 :',inputNum1 - inputNum2)

def mul():
    print('곱셈 결과 :',inputNum1 * inputNum2)

def div():
    print('나눗셈 결과 :',inputNum1 / inputNum2)

while True:
    input('아무키나 누르세요.')
    os.system('clear')
    selectOperator = int(input('연산자 선택. \n 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.종료\n - '))
    if(selectOperator == 5):
        print('The End!!!')
        exit()
    else:
        inputNum1 = float(input('첫번째 숫자를 입력 : '))
        inputNum2 = float(input('두번째 숫자를 입력 : '))    
        if(selectOperator == 1):
            add()
        elif(selectOperator == 2):
            sub()
        elif(selectOperator == 3):
            mul()
        elif(selectOperator == 4):
            div()
        else:
            print('Error')