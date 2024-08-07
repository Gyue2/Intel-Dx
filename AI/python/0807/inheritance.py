class Car:
    def __init__(self,make,model,color,price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    def setMake(self,make):
        self.make = make
    
    def getMake(self):
        return self.make
    
    def printInfo(self):
        return self.make + self.model + self.color + str(self.price)
    
class ElectricCar(Car):
        def __init__(self,make,model,color,price,batterySize):
            super().__init__(make,model,color,price)
            self.batterySize = batterySize

        def setBatterySize(self,batterySize):
            self.batterySize = batterySize
        
        def getBatterySize(self):
            return self.batterySize
        
        def printInfoElec(self):
            return super().printInfo() +str(self.batterySize)

def main():
    basicCar = Car('Hyundae ','Avante ','Black ',2000000)
    print(basicCar.printInfo())
    myCar = ElectricCar('Tisla ','Model S ','White ',10000,0)
    myCar.setMake('Tesla ')
    myCar.setBatterySize(60)
    print(myCar.printInfoElec())

main()