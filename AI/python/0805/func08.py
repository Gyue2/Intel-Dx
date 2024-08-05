def addFunc(num):
    if num > 0:
        print('num : ',num)
        addFunc(num - 1)
        print('num : ',num)
        
addFunc(10)