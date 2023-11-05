import pandas as pd
from geopy.distance import distance

apart = pd.read_csv("서울시 공동주택 아파트 정보.csv", encoding= 'cp949')
bus = pd.read_excel('서울시버스정류소위치정보(20230718).xlsx',sheet_name = 'Data')


apart = apart.rename(columns={'좌표X': '경도', '좌표Y': '위도'})
apart=apart.dropna(subset=["위도","경도"])
apart=apart.astype("str")


apart = apart[~(apart["위도"].str.contains(","))]
apart = apart[~(apart["경도"].str.contains(","))]



apart_xy=apart[['위도','경도',"번호"]]
bus_xy = bus.rename(columns={'X좌표': '경도', 'Y좌표': '위도'})
bus_xy = bus_xy[["ARS_ID",'위도','경도']]
bus=bus_xy


# #apart자리에는 무조건 apart넣어야됨
# def near(apart, bus):
#     nearNum = []
#     count = 0 
#     for i in range(len(apart)):
#         wd = apart.위도[i]
#         gd = apart.경도[i]
#         print(distance((wd,gd),(bus.위도[j],bus.경도[j])).kilometers)



apartitems={}
busitems={}
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


for i in range(len(bus)):
    itemdata = bus.iloc[i]

    originalnumber = itemdata["ARS_ID"]
    originalwido = itemdata["위도"]
    originalgyongdo = itemdata["경도"]

    _x = float(originalgyongdo) / per1_x
    _y = float(originalwido) / per1_y 
    if((int(_x,),int(_y)) not in busitems):
        busitems[(int(_x,),int(_y))] = [(originalnumber,originalwido,originalgyongdo)]
    else:
        busitems[(int(_x,),int(_y))].append((originalnumber,originalwido,originalgyongdo))

print(busitems)
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
            if((int(realX),int(realY)) in busitems):
                for p in busitems[(int(realX),int(realY))]:

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

f = open("nearBus.csv","w");
for x,y in searched.items():
    count = len(y)
    f.write(x +"," + str(count)+"\n")
f.close()