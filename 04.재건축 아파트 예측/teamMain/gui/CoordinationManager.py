'''
    주의 :
    이 프로그램은 제공 또는 서비스 목적이 아니며 외부 용도로 사용할 수 없음.
    이 프로그램을 외부에 공유 하거나 전달 할 수 없으며
    기타 라이선스 및 각종 정보가 확인 되지 않은 소스코드임.

    오직 공부 목적으로 사용함.
'''

import pandas as pd

class CoordinationManager:
    def __init__(self,fileName, xcolumn,ycolumn,busName, gapSize=1):
        self.__xcolumn = xcolumn
        self.__ycolumn = ycolumn
        self.__busName =busName

        self.__fileName = fileName
        self.__coordinations={}
        self.gapSize = gapSize
        pass


    def load(self):
        dataFrame = pd.read_csv(self.__fileName,encoding="UTF-8",header=0)
        df = dataFrame[[self.__xcolumn,self.__ycolumn,self.__busName]]
        df = df.dropna(subset=(self.__xcolumn,self.__ycolumn))

        df = df[~(df[self.__xcolumn].astype("str").str.contains(","))]
        df = df[~(df[self.__ycolumn].astype("str").str.contains(","))]
        _xLocation = self.__xcolumn
        _yLocation = self.__ycolumn
        df[self.__xcolumn] = df[self.__xcolumn].astype("float")
        df[self.__ycolumn] = df[self.__ycolumn].astype("float")

        _name = self.__busName

        _XSorted=[]
        _YSorted=[]

        for x in df.iloc:
            _x = x[_xLocation]
            _y = x[_yLocation]
            _y=-_y
            _nm = x[_name]
            _ox = int(_x//self.gapSize)
            _oy = int(_y//self.gapSize)
            if(len(_XSorted)==0):
                _XSorted=[_ox,_ox]
            if(len(_YSorted)==0):
                _YSorted=[_oy,_oy]
            if(_XSorted[0]>_ox):
                _XSorted[0]=_ox
            if(_XSorted[1]<_ox):
                _XSorted[1]=_ox
            if(_YSorted[0]>_oy):
                _YSorted[0]=_oy
            if(_YSorted[1]<_oy):
                _YSorted[1]=_oy

            if (_x,_y) not in self.__coordinations:
                self.__coordinations[(_ox,_oy)] = [(_x,_y,_nm)]
            else:
                self.__coordinations[(_ox,_oy)].append((_x,_y,_nm))
        print(len(self.__coordinations) ,"개의 격자 데이터 로드 됨")
        print("격자계산 X 범위", _XSorted[0],_XSorted[1])
        print("격자계산 Y 범위",_YSorted[0],_YSorted[1])
        return self


    def getItems(self, startX, startY, sizeXPerFullWidth, sizeYPerFullHeight):
        startX= int(startX// self.gapSize)
        startY= int(startY// self.gapSize)

        shouldGapXSize = int(sizeXPerFullWidth/self.gapSize)
        shouldGapYSize = int(sizeYPerFullHeight/self.gapSize)
        print("계산범위X: ", startX-1,startX+shouldGapXSize+1)
        print("범위Y: ", startY-1,startY+shouldGapYSize+1)
        #shouldGapSize는 화면에 적어도 격자가 몇개 포함되는지에 대한 정보입니다.

        items=[]
        for _x in range(startX-1,startX+shouldGapXSize+1):
            for _y in range(startY-1,startY+shouldGapYSize+1):
                if((_x,_y) in self.__coordinations):
                    for it in self.__coordinations[(_x,_y)]:
                        items.append(it)

        return items


