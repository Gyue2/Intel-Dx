balls = ['야구공','축구공','탁구공','골프공','농구공']
sports = ['basevall', 'basketvall','tennis','golf','soccer']
languages = ['c/c++','c#','python','java']

i = 0
for item in balls:
    print('item[{}] = {}'.format(i,item))
    i += 1

print('=============================')

for index, item in enumerate(balls):

    print(f'balls[{index}] = {item}',)

print(balls.index('축구공'))
print(balls[len(sports)-1])
print(languages.index('python'))
