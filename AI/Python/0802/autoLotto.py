import random

i = int(input("갯수 : "))
for _ in range(i):
    lotto = list(sorted(random.sample(range(1,46),6)))
    print(f'{_+1} : {lotto}')


