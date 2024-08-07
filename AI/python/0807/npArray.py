import numpy as np
import matplotlib.pyplot as plt


# 우리가 화씨 온도로 저장된 뉴욕의 기온 데이터를 얻었다고 하자. 
ftemp = [ 63, 73, 80, 86, 84, 78, 66, 54, 45, 63 ]

#이것을 넘파이로 배열로 변환하려면 다음과 같이 넘파이 모듈의 array() 함수를 호출한다.  
F = np.array(ftemp)
(F-32)*5/9
plt.plot(F)
plt.show()
