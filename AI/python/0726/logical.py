# logicValOne = True
# logicValTwo = False

logicValOne = bool(input("빈문자열은 False 아니면 True"))
logicValTwo = bool(input("빈문자열은 False 아니면 True"))


print("{}	{}".format(logicValOne,logicValTwo))
print("not logicValOne = {}, not logicValTwo = {}".format(logicValOne,(not logicValOne)))
print("{} and {} = {}".format(logicValOne, logicValTwo, (logicValOne and logicValTwo)))
print("{} or {} = {}".format(logicValOne, logicValTwo, (logicValOne or logicValTwo)))


# 논리 연산자는 논리값과 논리값을 연산해서 논리값을 리턴하는 연산자
# 입력은 True 혹은 False로 해야 함
