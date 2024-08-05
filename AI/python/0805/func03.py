def intorKor():
    print('안녕')

def introEng():
    print('Hello')

def introJap():
    print('こんにちは.')

selectNum = int(input('Where are U from? \n 1.한국 2. USA 3.Japan 4.End\n - '))
while True:
    if(selectNum == 1):
        intorKor()
    elif(selectNum == 2):
        introEng()
    elif(selectNum == 3):
        introJap()
    elif(selectNum == 4):
        print('End')
        break
    else:
        print('ERROR')
        break
    
