import random

rand_num = random.sample(range(1, 101), 10)


rand_num.sort()


print("정렬된 리스트:", rand_num)


print("제일 큰 수:", rand_num[-1])
print("제일 작은 수:", rand_num[0])
print(f'합 : {sum(rand_num)}')
print(f'평균 : {sum(rand_num)/len(rand_num)}')

import statistics
print('평균 : ', statistics.mean(rand_num))


import numpy
print(numpy.mean(rand_num))