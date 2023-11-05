'''
    주의 :
    이 프로그램은 제공 또는 서비스 목적이 아니며 외부 용도로 사용할 수 없음.
    이 프로그램을 외부에 공유 하거나 전달 할 수 없으며
    기타 라이선스 및 각종 정보가 확인 되지 않은 소스코드임.

    오직 공부 목적으로 사용함.
'''


import datetime
import datetime as dt
import math
import time
import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk

from GCViewer import GCViewer


class SubWindow:

    def __getFont(self,size):
        return ("NanumGothic",size)

    def setCallbackTranslateChange(self,action):
        self.translateCallback = action

    def setCallbackgetFlagXYCallback(self,action):
        self.getFlagXYCallback = action


    def __move(self):
        if(self.translateCallback!=None):
           self.translateCallback(float(self.__xCoord.get()), float(self.__yCoord.get()))

    def __view(self):
        flagCoord = self.getFlagXYCallback()
        strdata=""
        for x in self.__gcViewer.getItemsInRadius(flagCoord[0],-flagCoord[1],float(self.__radius.get())):
            strdata+= str(x[0]) +" " + str(x[1]) + " " + str(x[2]) + " " + str(x[3]) +"\n"
        tkinter.messagebox.showinfo("검색 결과",strdata)


    def __init__(self):
        window = Tk()
        window.geometry("400x700")
        window.title("건축 정보 보기")

        l1 = ttk.Label(window,text="좌표",font=self.__getFont(14))
        l1.place(x=50,y=20)
        self.__gcViewer = GCViewer("재개발_아파트.csv")
        self.__xCoord = ttk.Entry(window)
        self.__yCoord = ttk.Entry(window)
        self.__xCoord.place(x=50, y=50)
        self.__xCoord.insert(0,1)
        self.__yCoord.place(x = 200,y=50)
        self.__yCoord.insert(0,1)

        b1 = ttk.Button(window,text="이동",command=lambda : self.__move())
        b1.place(x=50,y=100)



        l1 = ttk.Label(window,text="계산을 원하는 반경 거리",font=self.__getFont(14))
        l1.place(x=50,y=200)

        self.__radius = ttk.Entry(window)
        self.__radius.place(x=50,y=250)
        self.__radius.insert(0,1)

        b2= ttk.Button(window,text="검색",command=lambda : self.__view())
        b2.place(x=50,y=300)



        pass

    def setXY(self,x,y):
        self.__xCoord.delete(0,END)
        self. __xCoord.insert(0, str(x))
        self.__yCoord.delete(0,END)
        self.__yCoord.insert(0, str(y))

    def setRadius(self,radius):
        self.__radius.delete(0,END)
        self.__radius.insert(0,str(radius))