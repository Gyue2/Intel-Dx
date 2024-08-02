import statistics

scores = []
hap = 0
for i in range(10):
    scores.append(int(input(f'{i+1}번 학생 점수 입력 : ')))
    hap += scores[i]
avg = statistics.mean(scores)
maxScore = max(scores)
minScore = min(scores)

for i in range(10):
    print(f'{i+1}번 학생의 성적 : {scores[i]}')

print('성적 합 =',hap)
print('성적 평균 =',avg)
print('최대값 = ',maxScore)
print('최솟값 = ',minScore)

print('특정 점수 이상의 학생 수 출력하기')
score = int(input('점수 입력 : '))
cnt = 0
for i in range(10):
    if scores[i] >= score:
        cnt += 1

print(scores)
print(f'{score}점 이상의 학생은 {cnt}명 입니다.')

