'''
    주의 :
    이 프로그램은 제공 또는 서비스 목적이 아니며 외부 용도로 사용할 수 없음.
    이 프로그램을 외부에 공유 하거나 전달 할 수 없으며
    기타 라이선스 및 각종 정보가 확인 되지 않은 소스코드임.

    오직 공부 목적으로 사용함.
'''

import random
import math
import time

coordinations=[]

def getDistance(startX, startY, endX, endY):
    for x in range(10):
        a=random.randint(1,10000000)


    return math.sqrt(math.pow(startX-endX,2) + math.pow(startY-endY,2))


for i in range(100000):
    coordinations.append((random.randint(0,10000),random.randint(0,10000)))


result=[]

latestTime = time.time()
for i in range(len(coordinations)):
    for j in range(len(coordinations)):
        distance= getDistance(coordinations[i][0],coordinations[i][1],coordinations[j][0],coordinations[j][1])
        if(distance<=10):
            result.append(distance)

    nowTime = time.time()
    timeDelta = nowTime-latestTime
    print(str(round(i/len(coordinations) * 100 ,2))+ "% 완료... (남은 시간 : " + str(round(float( timeDelta * (len(coordinations)-i) / 60 / 60),2)) + "시간 )")
    latestTime = nowTime



