import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('analyze_fourGu_21.csv')
df.sort_values(by='하루평균유동인구_대중교통',inplace=True)

#지지플랏
from plotnine import *
#한글 폰트
from matplotlib import font_manager, rc
font_path = r'C:\Users\LG\Desktop\exam_pandas\Day_07'+'\malgun.ttf'
font_name= font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)

#하루평균유동인구를 시각화
p1 = ggplot(df) + geom_bar(aes(x='매장명',y='하루평균유동인구_대중교통',fill = '인접_상가수'),stat='identity') + theme(text=element_text(fontproperties=font_name),axis_text_x=element_text(angle=60, hjust=1))
print(p1)

# 다른 요인이 뭐가 있을가 생각하니 인접상구수가 있어서 인접상가수를 그래프에 추가하여 시각화를 함
p2 = ggplot(df) + geom_bar(aes(x='매장명',y='인접_상가수',fill='하루평균유동인구_대중교통'),stat='identity') + theme(text=element_text(fontproperties=font_name),axis_text_x=element_text(angle=70, hjust=1))+ geom_hline(yintercept=347, linetype='dashed', color='red')
print(p2)

# 학교를 요인으로 시각화
p3 = ggplot(df) + geom_bar(aes(x='매장명',y='인접_학교수',fill='하루평균유동인구_대중교통'),stat='identity') + theme(text=element_text(fontproperties=font_name),axis_text_x=element_text(angle=70, hjust=1)) + geom_hline(yintercept=7.7, linetype='dashed', color='red')
print(p3)

# 양옆으로 한눈에 보기위해 시각화
fig, axs = plt.subplots(1,2,figsize= (15,6))
axs[0].bar(df['매장명'],df['인접_상가수'])
axs[1].bar(df['매장명'],df['인접_학교수'])
axs[0].set_xticks(range(len(df['매장명'])))
axs[1].set_xticks(range(len(df['매장명'])))
axs[0].set_xticklabels(df['매장명'].to_list(), rotation=42,ha='right')
axs[1].set_xticklabels(df['매장명'].to_list(), rotation=42,ha='right')
axs[0].set_title('인접_상가수')
axs[1].set_title('인접_학교수')
axs[0].axhline(347,color='red')
axs[1].axhline(7.7,color='red')
fig.tight_layout()
plt.show()


#인접 학교 수와 인접 매장이 적은 지점 중 겹치는 매장이 있는지 확인하고, 그 매장을 학교, 매장 수와는 다른 입지 조건이라고 판단한다. 인접 학교 수와 인접 매장수가 적은 스타벅스 매장이 가지고 있는 특징을 찾아본다.
mask = (df['인접_상가수'] <= 347) & (df['인접_학교수'] <= 7.7 ) & (df['하루평균유동인구_대중교통'] < 782.54)
smallDF=df[mask]
print(smallDF)

#대구 팔공산 : 관광객이나 자연과 아름다운 조화를 목적으로 입지한 것으로 보인다. 대구관광코스로도 공공데이터포털에 올라와있다.
palgong = pd.read_csv('대구광역시_관광코스 정보_20210906.csv',encoding='cp949')
print(palgong[palgong['코스 주제'] == '팔공산'][['코스타이틀','지역','관광지']])

#대구앞산DT: 지점 위치가 앞산 카페거리에 있다. 카페거리에 카페와 음식점 등이 몰려있기 때문에 스타벅스가 들어온것으로 보인다.
apsan = pd.read_csv('download.csv')
print(apsan)

#대구카톨릭대학교병원: 병원이라는 특수한 건물에 입지하였다. 이는 서울을 비롯한 다른지역에도 입지한 예가 많다.
hospital = pd.read_excel('스타벅스매장주소(20191029).xlsx')
print(hospital[hospital.지점명.str.contains('병원')])

#대구율하: 주변에 아파트 단지가 형성되어있어서 도보로 이용하는것 같음
ulha = pd.read_csv('대구광역시 동구_아파트 현황_20221213.csv',encoding='cp949')
print(ulha[ulha.주소.str.contains('율하')])

#테크노폴리스에 위치한 기업체
tech = pd.read_csv('대구광역시 달성군_기업체 현황_20211112.csv',encoding='cp949')
print(tech[tech.소재지주소.str.contains('테크노')])

#동대구로 DT는 예전 mbc네거리에 위치하고 주변에 아파트입주예정이 많은 지역에 위치하였고, 웨딩홀과 세무서가 있다.
