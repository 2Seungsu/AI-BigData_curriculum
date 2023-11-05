import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#폰트
from matplotlib import font_manager, rc
font_path = r'C:\Users\LG\Desktop\exam_pandas\Day_07'+'\malgun.ttf'
font_name= font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)


# 파일 불러오기
dague22 = pd.read_csv('analyze_Daegu_22.csv')
dague22.sort_values('하루평균유동인구_대중교통',ascending=False,inplace=True)

#중앙값을 대표값으로 설정
median_ = dague22['하루평균유동인구_대중교통'].median()

# 하루평균유동인구_대중교통 막대그래프
plt.figure(figsize=(10,8))
sns.barplot(x='매장명',y='하루평균유동인구_대중교통',data= dague22)
plt.ylabel('하루평균유동인구_대중교통',fontsize=20)
plt.axhline(median_, color='red', linestyle='dashed', linewidth=2, label='Median')

plt.gca().set_xticklabels([])
plt.gca().set_xlabel('')

plt.savefig('유동인구중앙값상한선.jpg')
plt.show()

print(f"유동인구 많은 지점의 하한선 : {median_}")


######################################
plt.figure(figsize=(10,8))
sns.barplot(x='매장명',y='하루평균유동인구_대중교통',data= dague22[dague22['하루평균유동인구_대중교통'] <= median_])
plt.ylabel('하루평균유동인구_대중교통',fontsize=20)
plt.axhline(median_, color='red', linestyle='dashed', linewidth=2, label='Median')
plt.xticks(ha='right',rotation=75)

plt.savefig('유동인구중앙값상한선1.jpg')
plt.show()

print(f"하한선보다 낮은 지점의 갯수 : {len(dague22[dague22['하루평균유동인구_대중교통'] <= median_])}개")