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




player_id= id[0]


def graph_(player_id):

    # 모듈 import
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # 파일 불러오기
    file_2018=r'C:\EXAM_PANDAS\soccerDF\soccer18 (1).csv'
    df_2018=pd.read_csv(file_2018)
    file_2019=r'C:\EXAM_PANDAS\soccerDF\soccer19 (1).csv'
    df_2019=pd.read_csv(file_2019)
    file_2020=r'C:\EXAM_PANDAS\soccerDF\soccer20 (1).csv'
    df_2020=pd.read_csv(file_2020)
    file_2021=r'C:\EXAM_PANDAS\soccerDF\soccer21 (1).csv'
    df_2021=pd.read_csv(file_2021)
    file_2022=r'C:\EXAM_PANDAS\soccerDF\soccer22 (1).csv'
    df_2022=pd.read_csv(file_2022)
    file_2023=r'C:\EXAM_PANDAS\soccerDF\soccer23 (1).csv'
    df_2023=pd.read_csv(file_2023)
    file_2024=r'C:\EXAM_PANDAS\soccerDF\soccer24 (1).csv'
    df_2024=pd.read_csv(file_2024)
    file_2025=r'C:\EXAM_PANDAS\soccerDF\soccer25 (1).csv'
    df_2025=pd.read_csv(file_2025)

    # df 생성
    df_player=pd.DataFrame()
    df_player['2018']=df_2018[df_2018['sofifa_id']==player_id].iloc[0]
    df_player['2019']=df_2019[df_2019['sofifa_id']==player_id].iloc[0]
    df_player['2020']=df_2020[df_2020['sofifa_id']==player_id].iloc[0]
    df_player['2021']=df_2021[df_2021['sofifa_id']==player_id].iloc[0]
    df_player['2022']=df_2022[df_2022['sofifa_id']==player_id].iloc[0]
    df_player['2023']=df_2023[df_2023['sofifa_id']==player_id].iloc[0]
    df_player['2024']=df_2024[df_2024['sofifa_id']==player_id].iloc[0]
    df_player['2025']=df_2025[df_2025['sofifa_id']==player_id].iloc[0]
    df_player=df_player.T

    player_name=df_player['name'][-1]
    df_player=df_player[['sofifa_id','overall','potential', 'value_eur', 'wage_eur']]

    # 단위 스케일링
    df_player['value_eur']=df_player['value_eur']/1000000
    df_player['wage_eur']=df_player['wage_eur']/1000
    
    df_player=np.floor(df_player).astype(int)

    # 그래프 그리기
    from matplotlib import font_manager

    fe = font_manager.FontEntry(
        #fname=r'C:\Users\KDP-26-\AppData\Local\Microsoft\Windows\Fonts\TENADA.ttf', # ttf 파일이 저장되어 있는 경로
        fname='./pred/Tenada.ttf',
        name='TENADA')                        # 이 폰트의 원하는 이름 설정
    font_manager.fontManager.ttflist.insert(0, fe)              # Matplotlib에 폰트 추가
    plt.rcParams.update({'font.size': 12, 'font.family': 'TENADA'}) # 폰트 설정

    fig, axes = plt.subplots(2,2, figsize=(15,10))

    axes[0,0].plot(df_player.index, df_player[df_player.columns[1]])
    axes[0,0].set_title(f'[{player_name}] Overall', size=25)
    axes[0,0].set_ylim(df_player[df_player.columns[1]].min()-10,df_player[df_player.columns[1]].max()+10)
    for i, v in enumerate(df_player[df_player.columns[1]]):
        axes[0,0].text(i, v, f'{v}', ha='center', va='bottom', size=15)

    axes[0,1].plot(df_player.index, df_player[df_player.columns[2]])
    axes[0,1].set_title(f'[{player_name}] Potential', size=25)
    axes[0,1].set_ylim(df_player[df_player.columns[2]].min()-10,df_player[df_player.columns[2]].max()+10)
    for i, v in enumerate(df_player[df_player.columns[2]]):
        axes[0,1].text(i, v, f'{v}', ha='center', va='bottom', size=15)

    axes[1,0].plot(df_player.index, df_player[df_player.columns[3]])
    axes[1,0].set_title(f'[{player_name}] Value', size=25)
    axes[1,0].set_ylim(df_player[df_player.columns[3]].min()-20,df_player[df_player.columns[3]].max()+20)
    axes[1,0].set_ylabel('백만', loc='top', rotation=0)
    for i, v in enumerate(df_player[df_player.columns[3]]):
        axes[1,0].text(i, v, f'{v}', ha='center', va='bottom', size=15)

    axes[1,1].plot(df_player.index, df_player[df_player.columns[4]])
    axes[1,1].set_title(f'[{player_name}] Wage', size=25)
    axes[1,1].set_ylim(df_player[df_player.columns[4]].min()-20,df_player[df_player.columns[4]].max()+20)
    axes[1,1].set_ylabel('천', loc='top', rotation=0)
    for i, v in enumerate(df_player[df_player.columns[4]]):
        axes[1,1].text(i, v, f'{v}', ha='center', va='bottom', size=15)

    plt.tight_layout()
    plt.show()

graph_(player_id)