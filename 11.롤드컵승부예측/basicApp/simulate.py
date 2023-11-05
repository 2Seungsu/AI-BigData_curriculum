import mariadb
import sys
from tqdm import tqdm
# MariaDB 연결 정보 설정
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    "port":3307,
    'database': 'db_ai'
}

# MariaDB에 연결
try:
    conn = mariadb.connect(**db_config)
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")

# 커서 생성
cursor = conn.cursor()

# 가져올 테이블 이름 설정
table_name = '롤드컵팀_능력치정규화'

# SQL 쿼리 실행 (테이블 데이터 가져오기)
query = f"SELECT * FROM {table_name}"
cursor.execute(query)

result = []
# 결과 데이터 읽기
for row in cursor:
    result.append(row)

# 연결 종료
conn.close()

# 데이터 ---------------------------------------------------
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


df=pd.DataFrame(result)
df.columns = ['Name','prob']
df.prob[4] = df.prob[4] -0.2
team_mapping = {
    'Bilibili Gaming': 'BLG',
    'T1': 'T1',
    'Gen.G eSports': 'GenG',
    'KT Rolster': 'KT',
    'JD Gaming': 'JDG',
    'GAM Esports': 'GAM',
    'LNG Esports': 'LNG',
    'Weibo Gaming': 'Weibo',
    'Dplus KIA': 'DK',
    'G2 Esports': 'G2',
    'MAD Lions': 'MAD',
    'Team BDS': 'BDS',
    'Cloud9': 'Cloud9',
    'Fnatic': 'Fnatic',
    'Team Liquid': 'TL',
    'NRG': 'NRG'
}
new_teams = [team_mapping[team] for team in df.Name]
df.Name = new_teams



# 우승확률 ---------------------------------------------------
def simulate_total(df):
    df = df.sample(frac=1)
    df = df.reset_index(drop=True)  # index 재설정

    round_number = 1
    teamList = []
    while len(df) > 1:
        #print(f"라운드 {round_number}")
        winners = []
        for i in range(0, len(df), 2):
            team1 = df.loc[i, 'Name']
            team2 = df.loc[i + 1, 'Name']
            teamList.append(team1)
            teamList.append(team2)


            prob1 = df.loc[i, 'prob'] + np.random.random()
            prob2 = df.loc[i + 1, 'prob'] + np.random.random()

            result = team1 if prob1 > prob2 else team2  # 확률에 따라 승자 결정

            prob1 = df.loc[i, 'prob']
            prob2 = df.loc[i + 1, 'prob']
            #print(f"{team1} vs {team2}: {result} 승리")
            winners.append(result)
        df = df[df['Name'].isin(winners)].reset_index(drop=True)
        round_number += 1
    #print(f"우승 팀: {winners[0]}")
    return winners[0], teamList



# 상대팀별 이길 확률 ---------------------------------------------------
def simulate_one(myTeam, yourTeam):
    teamA = []
    teamB = []
    for _ in tqdm(range(1000)):
        if  df.set_index('Name').loc[myTeam][0] + np.random.randn() > df.set_index('Name').loc[yourTeam][0] + np.random.randn():
            teamA.append(1)
            teamB.append(0)
        else:
            teamA.append(0)
            teamB.append(1)
    if sum(teamA)/len(teamA) > sum(teamB)/len(teamB):
        return f'VS {yourTeam}', '승',str(round(sum(teamA)/1000,2) * 100) + '%'
    else:
        return f'VS {yourTeam}', '패', str(round(sum(teamB)/1000,2) * 100) + '%'



