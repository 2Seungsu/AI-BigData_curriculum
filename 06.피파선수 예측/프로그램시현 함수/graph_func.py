import soccer


# 테스트용 임의 값 설정 -> 나중에 함수로 받기 ~
player_id=190871


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

    fig, axes = plt.subplots(4,1, figsize=(10,15))

    axes[0].plot(df_player.index, df_player[df_player.columns[1]])
    axes[0].set_title(f'[{player_name}] Overall', size=25)
    axes[0].set_ylim(df_player[df_player.columns[1]].min()-10,df_player[df_player.columns[1]].max()+10)
    for i, v in enumerate(df_player[df_player.columns[1]]):
        axes[0].text(i, v, f'{v}', ha='center', va='bottom', size=15)

    axes[1].plot(df_player.index, df_player[df_player.columns[2]])
    axes[1].set_title(f'[{player_name}] Potential', size=25)
    axes[1].set_ylim(df_player[df_player.columns[2]].min()-10,df_player[df_player.columns[2]].max()+10)
    for i, v in enumerate(df_player[df_player.columns[2]]):
        axes[1].text(i, v, f'{v}', ha='center', va='bottom', size=15)

    axes[2].plot(df_player.index, df_player[df_player.columns[3]])
    axes[2].set_title(f'[{player_name}] Value', size=25)
    axes[2].set_ylim(df_player[df_player.columns[3]].min()-20,df_player[df_player.columns[3]].max()+20)
    axes[2].set_ylabel('백만', loc='top', rotation=0)
    for i, v in enumerate(df_player[df_player.columns[3]]):
        axes[2].text(i, v, f'{v}', ha='center', va='bottom', size=15)

    axes[3].plot(df_player.index, df_player[df_player.columns[4]])
    axes[3].set_title(f'[{player_name}] Wage', size=25)
    axes[3].set_ylim(df_player[df_player.columns[4]].min()-20,df_player[df_player.columns[4]].max()+20)
    axes[3].set_ylabel('천', loc='top', rotation=0)
    for i, v in enumerate(df_player[df_player.columns[4]]):
        axes[3].text(i, v, f'{v}', ha='center', va='bottom', size=15)

    plt.tight_layout()
    plt.show()

graph_(player_id)