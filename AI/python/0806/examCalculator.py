def getTotalScore(s1,s2,s3):
    return s1 + s2 + s3

def getAverageScore(s1,s2,s3):
    return getTotalScore(s1,s2,s3)/3

def getPassFail(s1,s2,s3):

    if(getAverageScore(s1,s2,s3) >= 60):
        return 'Pass'
    
    return 'Fail'