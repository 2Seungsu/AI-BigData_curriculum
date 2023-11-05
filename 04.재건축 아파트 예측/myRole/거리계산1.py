import pandas as pd
from geopy.distance import distance

apart = pd.read_csv("서울시 공동주택 아파트 정보.csv", encoding= 'cp949')
station = pd.read_csv('서울시 역사마스터 정보.csv',encoding='cp949')


# apart = apart.rename(columns={'좌표X': '경도', '좌표Y': '위도'})
# apart['k-사용검사일-사용승인일'] = 2023 - apart['k-사용검사일-사용승인일'].astype('datetime64').dt.year
# apart = apart[apart['k-사용검사일-사용승인일']>=30]

apart=apart.dropna(subset=["위도","경도"])
apart=apart.astype("str")


apart = apart[~(apart["위도"].str.contains(","))]
apart = apart[~(apart["경도"].str.contains(","))]



apart_xy=apart[['위도','경도',"번호"]]
station_xy = station[["역사_ID",'위도','경도']]



# #apart자리에는 무조건 apart넣어야됨.
# def near(apart, bus):
#     nearNum = []
#     count = 0 
#     for i in range(len(apart)):
#         wd = apart.위도[i]
#         gd = apart.경도[i]
#         print(distance((wd,gd),(bus.위도[j],bus.경도[j])).kilometers)



apartitems={}
stationitems={}
per1_x = 0.010966
per1_y = 0.009013


x_km = 0.5
y_km = 0.5

for i in range(len(apart)):
    itemdata = apart.iloc[i]

    originalnumber = itemdata["번호"]
    originalwido = itemdata["위도"]
    originalgyongdo = itemdata["경도"]

    _x = float(originalgyongdo) / per1_x
    _y = float(originalwido) / per1_y 
    if((int(_x,),int(_y)) not in apartitems):
        apartitems[(int(_x,),int(_y))] = [(originalnumber,originalwido,originalgyongdo)]
    else:
        apartitems[(int(_x,),int(_y))].append((originalnumber,originalwido,originalgyongdo))


for i in range(len(station)):
    itemdata = station.iloc[i]

    originalnumber = itemdata["역사_ID"]
    originalwido = itemdata["위도"]
    originalgyongdo = itemdata["경도"]

    _x = float(originalgyongdo) / per1_x
    _y = float(originalwido) / per1_y 
    if((int(_x,),int(_y)) not in stationitems):
        stationitems[(int(_x,),int(_y))] = [(originalnumber,originalwido,originalgyongdo)]
    else:
        stationitems[(int(_x,),int(_y))].append((originalnumber,originalwido,originalgyongdo))

print(stationitems)
a=0

searched={}
for i in range(len(apart)):
    a+=1
    print(i/len(apart) * 100 ,"퍼센트 완료.")
    itemdata = apart.iloc[i]
    
    originalnumber = itemdata["번호"]
    originalwido = itemdata["위도"]
    originalgyongdo = itemdata["경도"]
    
    
    _x = float(originalgyongdo) / per1_x
    _y = float(originalwido) / per1_y 
    
    center_x = int(_x)
    center_y = int(_y)
    print("탐색 ->",originalnumber,center_x,center_y)
    for realX in range(center_x - 3, center_x+3,1):
        for realY   in range(center_y - 3, center_y+3,1):
            if((int(realX),int(realY)) in stationitems):
                for p in stationitems[(int(realX),int(realY))]:

                    if(distance((float(originalwido),float(originalgyongdo)),(p[1],p[2])).kilometers <= 1):
                        if(originalnumber in searched):
                            searched[originalnumber].append(p[0])
                        else:
                            searched[originalnumber] =[p[0]]



print(searched)

        


# # print(len(items))
# print("아이템 0 ", data[0])
# print("아이템 1", data[1])

# print(distance((float(data[0]["위도"]),float(data[0]["경도"])),(float(data[1]["위도"]),float(data[1]["경도"]))).kilometers)



# for i in range(len(apart)):
#     wd = apart.위도[i]
#     gd = apart.경도[i]
    
# near(apart_xy,station_xy)

f = open("nearSt.csv","w");
for x,y in searched.items():
    count = len(y)
    f.write(x +"," + str(count)+"\n")
f.close()