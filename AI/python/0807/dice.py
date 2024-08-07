from random import randint

class Dice:

    def __init__(self,x,y):
        self._x = x
        self._y = y
        self._size = 30
        self._value = 1

    def getDiceValue(self):
        return self._value
    def printDice(self):
        print('주사위의 값 = ',self._value)
    def rollDice(self):
        self._value = randint(1,6)
d1 = Dice(100,100)
d1.rollDice()
d1.printDice()
