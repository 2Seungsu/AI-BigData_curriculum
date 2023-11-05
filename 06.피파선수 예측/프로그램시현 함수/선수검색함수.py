# 파일
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:\EXAM_PANDAS\soccerDF\soccer5252.csv')
# df['player_url'] = df.player_url.apply(lambda x: x.replace('220002','220818'))
# df.player_url[5]
# df.position = ['FW' if 'S' in i or 'W' in i else 'MID' if 'M' in i else 'DF' if 'B' in i else 'GK'  for i in df.position]

# # URL 접속
import webbrowser
# webbrowser.open(df.player_url[7])

from matplotlib import font_manager
import matplotlib.pyplot as plt

fe = font_manager.FontEntry(
    fname=r'C:\Users\User\Documents\카카오톡 받은 파일\TENADA.ttf', # ttf 파일이 저장되어 있는 경로
    name='TENADA')                        # 이 폰트의 원하는 이름 설정
font_manager.fontManager.ttflist.insert(0, fe)              # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 12, 'font.family': 'TENADA'}) # 폰트 설정

def search_players_by_market_value(market_value=df.overall, position = None, weekly_wage=None, abilities=None, potential=None):
    # 여기에 시장가치를 이용하여 검색하는 코드를 작성합니다.
    # 예: 시장가치를 기준으로 데이터베이스에서 선수 검색
    
    # valueList = df.value23.values
    # valueList.sort()
    # valueList = valueList[::-1]
    for a in range(len(df)):
        if market_value >= df.overall[a]:
            resultDF = df[a:a+10]
            print (resultDF)
            
            #return df.sofifa_id[a:a+10]
            break

    num = int(input ('맘에 드는 선수 있습니까? sofifaid를 입력해주세오. : '))
    webbrowser.open(df[df.sofifa_id == num].player_url.values[0])
    num1 = input ('선수를 구매하시겠습니까?(y or n) : ')
    idList = []
    nameList = []
    if num1 == 'y':
        idList.append(int(num))
        nameList.append(df[df.sofifa_id == num].name.values[0])

    print (nameList)
    return idList

print (f'\n============================== 선수 찾으시옷 =================================')
search = input ('선수 능력치 검색 : ')
id = search_players_by_market_value(int(search))