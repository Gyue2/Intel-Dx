import statistics

scores = [int(input(f'{i+1}번 학생 점수 입력 : ')) for i in range(10)]
hap = sum(scores)
avg = statistics.mean(scores)
maxScore = max(scores)
minScore = min(scores)

for i, score in enumerate(scores):
    print(f'{i+1}번 학생의 성적 : {score}')

print('성적 합 =', hap)
print('성적 평균 =', avg)
print('최대값 =', maxScore)
print('최솟값 =', minScore)

print('특정 점수 이상의 학생 수 출력하기')
score = int(input('점수 입력 : '))
cnt = sum(1 for s in scores if s >= score)

print(scores)
print(f'{score}점 이상의 학생은 {cnt}명 입니다.')