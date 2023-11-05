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
import tkinter as tk
import tkinter.ttk as ttk

import random as rd

import tkinter.messagebox

from CoordinationManager import CoordinationManager
from SubWindow import SubWindow


class GameObject:
    def __init__(self, canvas,canOverFlow=False):
        self.__canvas=canvas
        self.x=0
        self.y=0
        self.lastX=0
        self.lastY=0
        self.__standardX=0
        self.__standardY=0
        self.__scale=1
        self.canOverFlow=canOverFlow

        self.box=0
        pass

    def create(self, width, height,msg, color="white"):
        self.box = self.__canvas.create_rectangle(0,0,width,height,fill=color)
        self.__text = self.__canvas.create_text(0,0, fill="white", font="NanumGothic",anchor="w", text=msg)
        self.__objectWidth=width
        self.__objectHeight=height

        return self

    def delete(self):
        self.__canvas.delete(self.box)
        self.__canvas.delete(self.__text)

    def setStandardLocation(self,_x,_y):
        self.__standardY=_y
        self.__standardX=_x

    def setScale(self,_scale):
        self.__scale=_scale
    def moveX(self,x):
        self.x+=x
        if(int(self.lastX) != int(self.x)):
            self.update()

        self.lastX=self.x

    def moveY(self,y):
        self.y+=y

        if(int(self.lastY) != int(self.y)):
            self.update()
        self.lastY=self.y

    def setY(self,y):
        self.y=y


        if(int(self.lastY) != int(self.y)):
            self.update()
        self.lastY=self.y

    def setX(self, x):
        self.x =  x

        if (int(self.lastX) != int(self.x)):
            self.update()
        self.lastX = self.x

    def setXY(self,x,y):
        self.x=x
        self.y=y


        if (int(self.lastX) != int(self.x))  or (int(self.lastY) != int(self.y)):
            self.update()

        self.lastX=self.x
        self.lastY=self.y

    def moveXY(self,x,y):
        self.x+=x
        self.y+=y

        if (int(self.lastX) != int(self.x))  or (int(self.lastY) != int(self.y)):
            self.update()

        self.lastX=self.x
        self.lastY=self.y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def update(self):
        self.__canvas.moveto(self.box,  self.x*self.__scale -self.__standardX*self.__scale-15 ,  self.y*self.__scale -self.__standardY *self.__scale)
        self.__canvas.moveto(self.__text,  self.x*self.__scale -self.__standardX*self.__scale ,  self.y*self.__scale -self.__standardY *self.__scale)

class CircleObject:
    def __init__(self,canvas):
        self.canvas = canvas
        self.oval = None
        self._x=0
        self._y=0
        self.__standardX=0
        self.__standardY=0
        self.__scale=1
        self._radius=5

    def setX(self,x,y):
        self._x=x
        self._y=y
        self.update()
    def getRadiusByKM(self):
        per1_x = 0.010966
        per1_y = 0.009013
        xyv = math.sqrt(per1_x ** 2 + per1_y ** 2)
        return self._radius/xyv

    def setRadius(self,radius):
        self._radius=radius
        self.update()

    def getRadius(self):
        return self._radius

    def setStandardLocation(self,_x,_y):
        self.__standardY=_y
        self.__standardX=_x

    def setScale(self,_scale):
        self.__scale=_scale

    def update(self):
        if(self.oval is not None):
            self.canvas.delete(self.oval)

        srcX= (self._x*self.__scale) -(self._radius*self.__scale)  -  self.__standardX*self.__scale
        srcY= (self._y*self.__scale)-(self._radius*self.__scale) - self.__standardY*self.__scale
        dstX= (self._x*self.__scale)+(self._radius*self.__scale) - self.__standardX*self.__scale
        dstY= (self._y*self.__scale)+(self._radius*self.__scale) - self.__standardY*self.__scale
        print("현재 반지름",self._radius)
        print("시작 좌표 : " , srcX, srcY, dstX,dstY,)
        self.oval= self.canvas.create_oval(srcX,srcY,dstX,dstY, fill='', outline='green', width=3)



class TextObject:
    def __init__(self, canvas):
        self.canvas=canvas

    def create(self,x,y,msg, color="white"):
        self._id = self.canvas.create_text(x,y, fill=color, font="NanumGothic",anchor="w", text=msg)
        return self

    def changeText(self, msg):
        self.canvas.itemconfig(self._id, text=msg)

class GameMain:
    def __init__(self):
        self.downKeys = set()
        self.lastRenderedUnixTime =time.time()
        self.lastFPSUnixTime = time.time()
        self.__fpsCount=0
        self.__selfItem = SubWindow()
        self.__selfItem.setCallbackgetFlagXYCallback(lambda : (self.__flagX,self.__flagY))
        self.__selfItem.setCallbackTranslateChange(lambda x,y : self.__updateTranslate(x,y))
        window=tk.Tk()
        window.resizable(0,0)
        window.title("건축 정보 보기")
        window.bind("<KeyPress>", self.keyDown)
        window.bind("<KeyRelease>",self.keyRelease)
        window.bind("<Motion>",self.mouseMove)
        window.bind("<ButtonPress-1>",self.mouseDown)
        window.bind("<ButtonRelease-1>",self.mouseUp)
        canvas = tk.Canvas(window,width=700, height=700, bg="black")
        self.__latestMouse=(0,0)

        canvas.pack()
        self.__wd = 700
        self.__wh = 700

        window.focus_force()
        self.canvas = canvas
        self.window= window

        self.isGamePlay=True
        self.__initGameObjects()


        self.__isMovementMode=False
        self.__isChangeRadiusMode=False
        self.__translateX=126.9598728435
        self.__translateY=-37.556804829

        self.__latestTranslateX=self.__translateX
        self.__latestTranslateY=self.__translateY


        self.__gapSize =  0.02
        self.__scale=35000

        self.__cdm = [("WHITE",CoordinationManager("서울시버스정류소위치정보(20230718).csv","X좌표","Y좌표","정류소명",0.002).load()),
                      ("BLUE", CoordinationManager("서울시 공동주택 아파트 정보.csv", "좌표X", "좌표Y", "k-아파트명", 0.002).load()),
                      ]

    def isGamePlaying(self):
        return self.isGamePlay

    def __initGameObjects(self):
        canvas = self.canvas

        self.__circleObject = CircleObject(canvas)

        self.__flagItem = GameObject(canvas,False)
        self.__flagItem.create(10,10,"플래그","RED")

        self.__fpsText = TextObject(canvas).create(10,20,"FPS")
        self.__systemText = TextObject(canvas).create(10,50,"시스템 내부","LIGHTGREEN")

        self.__startTime=time.time()
        self.__objects=[]


    def setFlagLocation(self,cursorX,cusorY):

        self.__flagX = self.__translateX + self.latestMouseX / self.__wd * self.__gapSize
        self.__flagY = self.__translateY + self.latestMouseY / self.__wd * self.__gapSize
        self.__flagItem.setXY(self.__flagX, self.__flagY)
        self.__circleObject.setX(self.__flagX,self.__flagY)
        self.updateFlagLocation()


    def updateFlagLocation(self):
        self.__flagItem.setScale(self.__scale)
        self.__flagItem.setStandardLocation(self.__translateX, self.__translateY)
        self.__flagItem.update()

    def updateCircleLocation(self):

        self.__circleObject.setScale(self.__scale)
        self.__circleObject.setStandardLocation(self.__translateX, self.__translateY)
        self.__circleObject.update()

    def keyDown(self,event):
        if event.keycode not in self.downKeys:
            self.downKeys.add(event.keycode)



    def keyRelease(self,event):
        if event.keycode in self.downKeys:
            self.downKeys.remove(event.keycode)

    def mouseDown(self,event):
        print("down")
        if(16 in self.downKeys):
            self.__isMovementMode=True

        elif(17 in self.downKeys):
            self.__isChangeRadiusMode=True
            self.__latestRadiusX = self.latestMouseX
            self.__latestRadiusY = self.latestMouseY
            self.setFlagLocation(self.latestMouseX,self.latestMouseY)



        pass

    def isShowingCulling(self,x,y,translateX,translateY):
        start_wx,start_wy,end_wx,end_wy= translateX, translateY, translateX + self.__gapSize, translateY + self.__gapSize
        print(x,y,start_wx,start_wy,end_wx,end_wy)
        if(start_wx<=x<=end_wx and start_wy<=y<=end_wy):
            return True
        else:
            return False


    def __updateTranslate(self,x,y):
        self.__translateY=y
        self.__translateX=x
        self.__updateLocation()
    def __updateLocation(self):

        for x in range(len(self.__objects) - 1, -1, -1):
            x_i = self.__objects[x]
            if (self.isShowingCulling(x_i.getX(), x_i.getY(), self.__translateX, self.__translateY) == False):
                x_i.delete()
                self.__objects.pop(x)

        for p in self.__cdm:
            xColor = p[0]
            xManager = p[1]

            items2 = xManager.getItems(self.__translateX, self.__translateY, self.__gapSize, self.__gapSize)
            for x in items2:

                if (self.isShowingCulling(x[0], x[1], self.__latestTranslateX,
                                          self.__latestTranslateY) == False):
                    go = GameObject(self.canvas).create(10, 10, x[2], xColor)
                    go.setXY(x[0], x[1])
                    self.__objects.append(go)
                    # print("새 데이터 ", x)

                    go.setScale(self.__scale)
                    go.setStandardLocation(self.__translateX, self.__translateY)
                    go.update()
        self.__latestTranslateX = self.__translateX
        self.__latestTranslateY = self.__translateY
        self.__selfItem.setXY(self.__translateX, self.__translateY)


        self.__flagItem.setScale(self.__scale)
        self.__flagItem.setStandardLocation(self.__translateX, self.__translateY)
        self.__flagItem.update()

        self.updateCircleLocation()
        self.window.title("뷰어 - " + str(self.__translateX) + "," + str(-self.__translateY))

    def mouseUp(self,event):
        if(self.__isMovementMode):
            self.__isMovementMode=False
            self.__updateLocation();

        if(self.__isChangeRadiusMode):
            self.__isChangeRadiusMode=False

        pass
        #self.__circleObject.setRadius(0.001)


    def mouseMove(self,event):

        x, y = event.x, event.y
        self.latestMouseX = x
        self.latestMouseY=y

        if(self.__isMovementMode):
            x, y = event.x, event.y

            deltaX = x-self.__latestMouse[0]
            deltaY = y-self.__latestMouse[1]

            #scale=self.__gapSize
            self.__translateX-=deltaX / self.__scale
            self.__translateY -= deltaY/ self.__scale;
            print(self.__translateX, self.__translateY)

            self.__selfItem.setXY(self.__translateX, self.__translateY)
            self.updateFlagLocation()
            for x in self.__objects:
                x.setScale(self.__scale)
                x.setStandardLocation(self.__translateX, self.__translateY)
                x.update()

            self.updateCircleLocation()
        if(self.__isChangeRadiusMode):

            deltaX = x-self.__latestRadiusX
            deltaY = y-self.__latestRadiusY

            per1_x = 0.010966
            per1_y = 0.009013
            xyv = math.sqrt(per1_x**2 + per1_y**2)

            # resultX = deltaX* self.__gapSize *per1_x
            # resultY = deltaY* self.__gapSize*per1_y
            # radiusValue = math.sqrt(resultX**2 + resultY**2)
            radiusValue = math.sqrt(deltaX**2 + deltaY**2)/math.sqrt(self.__wd**2+self.__wh**2) * xyv

            self.__circleObject.setRadius(radiusValue)
            self.__selfItem.setRadius(self.__circleObject.getRadiusByKM())



        self.__latestMouse =( event.x, event.y)


    def update(self,timedelta):
        pass

    def dispose(self):
        self.window.destroy()

    def render(self):
        if(self.isGamePlay==False):
            return

        nowRenderTime = time.time()
        gapRenderTime = (nowRenderTime-self.lastRenderedUnixTime)
        if(gapRenderTime==0):
            return
        self.__fpsCount+=1
        if(nowRenderTime-self.lastFPSUnixTime>=1):
            self.__fpsText.changeText("FPS : " + str(self.__fpsCount))
            self.__fpsCount=0
            self.lastFPSUnixTime =nowRenderTime
        if(self.__latestMouse != None):
            self.__systemText.changeText("내부 오브젝트 객체 : " +str(len(self.__objects)) + "/ 마우스 좌표 : " + str(self.__latestMouse) +"/ 반지름 " + str(round(self.__circleObject.getRadiusByKM(),2)) +"km")
        time.sleep(1/120 )
        self.update(gapRenderTime)
        self.window.update()
        self.lastRenderedUnixTime= nowRenderTime

    def getAliveSecond(self):
        nowRenderTime = time.time()
        return str(round(nowRenderTime - self.__startTime, 2))

    def getScore(self):
        return str(self.__projectileLauncher.getDeleteItemCount() * 100)

    def __gameOver(self):
        self.isGamePlay = False



gm = GameMain()
while(1):
    if(gm.isGamePlaying()==False):
        break
    gm.render()
nowTime = datetime.datetime.now()
gm.dispose()

