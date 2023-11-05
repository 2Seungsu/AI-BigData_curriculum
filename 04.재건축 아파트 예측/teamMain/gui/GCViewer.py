'''
    주의 :
    이 프로그램은 제공 또는 서비스 목적이 아니며 외부 용도로 사용할 수 없음.
    이 프로그램을 외부에 공유 하거나 전달 할 수 없으며
    기타 라이선스 및 각종 정보가 확인 되지 않은 소스코드임.

    오직 공부 목적으로 사용함.
'''


import pandas as pd
import math
class GCViewer:
    def __init__(self, fileName):
        df = pd.read_csv("재개발_아파트.csv",encoding="UTF-8")
        self.df = df[["k-아파트명","좌표X","좌표Y","재개발 점수"]]

    def getItemsInRadius(self,center_x,center_y,km):
        result=[]
        print(km ,"로 탐색")
        for x in self.df.iloc:
            apartName = x["k-아파트명"]
            xLoc=float(x["좌표X"])
            yLoc = float(x["좌표Y"])
            score = x["재개발 점수"]

            per1_x = 0.010966
            per1_y = 0.009013
            xyv = math.sqrt(per1_x ** 2 + per1_y ** 2)


            print("거리 차이 : " ,math.sqrt((xLoc-center_x )**2 + (yLoc-center_y)**2) /xyv ,"km")
            if(math.sqrt((xLoc-center_x )**2 + (yLoc-center_y)**2) /xyv<=km):
                result.append((apartName,xLoc,yLoc,score))
        return result
