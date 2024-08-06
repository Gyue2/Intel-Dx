def printAverageScore(*scores):
    
    totalScore = 0
    cnt = len(scores)
    while True:
        for score in scores:
            totalScore += score
