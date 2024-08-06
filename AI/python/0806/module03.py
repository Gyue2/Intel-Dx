import examCalculator

score1 = int(input('1과목 점수 입력 :'))
score2 = int(input('2과목 점수 입력 :'))
score3 = int(input('3과목 점수 입력 :'))

print('총점 : ',examCalculator.getTotalScore(score1,score2,score3))
print('평균 : ',examCalculator.getAverageScore(score1,score2,score3))
print('합격여부 : ',examCalculator.getPassFail(score1,score2,score3))