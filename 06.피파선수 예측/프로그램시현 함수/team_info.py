import pandas as pd 
import numpy as np 
import warnings
warnings.filterwarnings('ignore')
# gk, df1, df2, df3, df4, mid1, mid2, mid3, fw1, fw2, fw3
# 193041 216267 231281 239818 189332 215914 200145 212622 239085 179813 230142

def find_team(gk, df1, df2, df3, df4, mid1, mid2, mid3, fw1, fw2, fw3):
    # gk=input('선수ID를 입력하세요.(골키퍼 1명)')
    # df1=input('선수ID를 입력하세요.(수비수 1명)')
    # df2=input('선수ID를 입력하세요.(수비수 1명)')
    # df3=input('선수ID를 입력하세요.(수비수 1명)')
    # df4=input('선수ID를 입력하세요.(수비수 1명)')
    # mid1=input('선수ID를 입력하세요.(미드필더 1명)')
    # mid2=input('선수ID를 입력하세요.(미드필더 1명)')
    # mid3=input('선수ID를 입력하세요.(미드필더 1명)')
    # fw1=input('선수ID를 입력하세요.(공격수 1명)')
    # fw2=input('선수ID를 입력하세요.(공격수 1명)')
    # fw3=input('선수ID를 입력하세요.(공격수 1명)')
    

    filename = r'C:\EXAM_PANDAS\soccerDF\players_23.csv'
    filename1=r'C:\EXAM_PANDAS\soccerDF\footballclub_2023_top180.csv'

    playDF=pd.read_csv(filename)
    teamDF=pd.read_csv(filename1)

    teamDF = teamDF.drop(columns=['FW','MID','DF'])
    teamDF['rank'] = (teamDF['TOTAL_MEAN'].rank(method='min', ascending=False)).astype('int64')

    overDF=playDF[(playDF['overall']>=70) & (playDF['overall']<=85)]
    gkDF=overDF[overDF['position']=='GK']
    dfDF=overDF[overDF['position']=='DF']
    midDF=overDF[overDF['position']=='MID']
    fwDF=overDF[overDF['position']=='FW']

    elveDF = pd.DataFrame(overDF)
    elveDF = elveDF.drop(elveDF.index)

    elveDF = elveDF.append(gkDF[gkDF['sofifa_id']==gk], ignore_index=True)
    elveDF = elveDF.append(dfDF[dfDF['sofifa_id']==df1], ignore_index=True)
    elveDF = elveDF.append(dfDF[dfDF['sofifa_id']==df2], ignore_index=True)
    elveDF = elveDF.append(dfDF[dfDF['sofifa_id']==df3], ignore_index=True)
    elveDF = elveDF.append(dfDF[dfDF['sofifa_id']==df4], ignore_index=True)
    elveDF = elveDF.append(midDF[midDF['sofifa_id']==mid1], ignore_index=True)
    elveDF = elveDF.append(midDF[midDF['sofifa_id']==mid2], ignore_index=True)
    elveDF = elveDF.append(midDF[midDF['sofifa_id']==mid3], ignore_index=True)
    elveDF = elveDF.append(fwDF[fwDF['sofifa_id']==fw1], ignore_index=True)
    elveDF = elveDF.append(fwDF[fwDF['sofifa_id']==fw2], ignore_index=True)
    elveDF = elveDF.append(fwDF[fwDF['sofifa_id']==fw3], ignore_index=True)


    same_mean=teamDF[teamDF['TOTAL_MEAN']==elveDF['overall'].mean()]
    elveDF = elveDF[['name','position','overall','potential']]
    print(elveDF)
    print(same_mean)

print (f'\n============================== 팀 만드시옷 =================================')
find_team(193041, 216267, 231281, 239818, 189332, 215914, 200145, 212622, 239085, 179813, 230142)