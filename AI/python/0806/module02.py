import converUnitModule

inputData = int(input('길이(mm)를 입력 :  '))

result = converUnitModule.converUnit(inputData)
converUnitModule.printLength(inputData,result)
