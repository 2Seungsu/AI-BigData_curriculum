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


gridLocation ={}
for i in range(len(coordinations)):
    coord = coordinations[i]
    _ox = coord[0]
    _oy = coord[1]
    _x = int(_ox/10)
    _y = int(_ox/10)
    if (_x,_y) in gridLocation:
        gridLocation[(_x,_y)].append((_ox,_oy))
    else:
        gridLocation[(_x,_y)] =[_ox,_oy]


print(gridLocation)

result ={}
latestTime = time.time()
counts=0
for i in range(len(coordinations)):
    coord = coordinations[i]
    _ox = coord[0]
    _oy = coord[1]
    _x = int(_ox/10)
    _y = int(_ox/10)

    for nowX in range(_x-3,_x+3):
        for nowY in range(_y-3,_y+3):
            if (nowX, nowY) in gridLocation:
                _dstCoord = gridLocation[(nowX, nowY)]
                distance = getDistance(_ox,_oy,_dstCoord[0],_dstCoord[1])
                if (distance <= 10):
                    if((_ox,_oy) in result):
                        result[(_ox,_oy)].append((_dstCoord[0],_dstCoord[1]))
                    else:
                        result[(_ox, _oy)]=[(_dstCoord[0],_dstCoord[1])]

    counts+=1
    nowTime = time.time()
    timeDelta = nowTime-latestTime
    if(timeDelta>=0.5):
        print(str(round(i/len(coordinations) * 100 ,2))+ "% 완료... (남은 시간 : " + str(round(float( timeDelta/counts * (len(coordinations)-i)),2)) + "초 )")
        latestTime = nowTime
        counts=0

print(result)