'''

    경고
    이 소스코드는 오직 빅데이터 4기의 데이터 분석 및
    인터넷 파싱 연습을 위한 용도 및 과제 용도로,

    외부 서비스에 대한 디컴파일,
    리버싱, 분해, 작업 등을 의미하지 않습니다.

    즉 단순 공개된 자료에 대한 분석일 뿐
    기타 목적으로 외부에 배포하거나 공개 용도로 작성되지 아니합니다.

    따라서 본 소스코드는 다른 서비스사의
    서비스를 방해할 목적이 전혀 아니며 개인 공부 용도로 사용됨을 명시합니다.

    본 소스코드는 있는 그대로(ASIS) 업로드되며,
    이용 및 참고에 대한
    발생할 수 있는 그 모든 문제에 대해서
    소스코드 작성자는 책임지지 아니합니다.

'''

import matplotlib.pyplot as plt
from konlpy.tag import Okt
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
prop = font_manager.FontProperties(fname="NanumGothic.ttf")
rc("font",family="NanumGothic")

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd

def process(df):
    print("0번 실행")
    data=[]
    a=0

    for x in df.iloc:
        a+=1
        okt = Okt()
        okt_tags = okt.pos(str(x["CONTENT"]), norm=True, stem=True)
        for word, tag in okt_tags:
            if (tag == "Noun"):
                data.append(word)
        print(a,df["CONTENT"].count())
    ct = Counter(data)
    items = ct.most_common(30)



    wc = WordCloud(font_path="E:/NanumGothic.ttf",background_color="white", max_font_size=60)
    cloud = wc.generate_from_frequencies(dict(items))

    plt.figure(figsize=(1.2,1.2),dpi=1000)
    plt.axis("off")
    plt.imshow(cloud)
    plt.show()

def process2(df):
    print("1번 실행")
    data=[]
    a=0

    for x in df.iloc:
        a+=1
        okt = Okt()
        okt_tags = okt.pos(str(x["TITLE"]), norm=True, stem=True)
        for word, tag in okt_tags:
            if (tag == "Noun"):
                data.append(word)
        print(a,df["CONTENT"].count())
    ct = Counter(data)
    items = ct.most_common(30)



    wc = WordCloud(font_path="E:/NanumGothic.ttf",background_color="white", max_font_size=60)
    cloud = wc.generate_from_frequencies(dict(items))

    plt.figure(figsize=(1.2,1.2),dpi=1000)
    plt.axis("off")
    plt.imshow(cloud)
    plt.show()


# def process3(df):
#     try:
#         data=[]
#         a=0
#         fig = plt.figure(figsize=(1.5,1.5),dpi=200)
#         ax = fig.add_subplot(1,1,1)
#
#         values=df["URL"].value_counts()
#         ax.bar([x for x in range(len(values.index.to_list()))],values)
#         ax.set_xticks([x for x in range(len(values.index.to_list()))])
#         ax.set_xticklabels(values.index.to_list())
#
#         plt.show()
#     except Exception as e:
#         print(e)
#
# def process4(df):
#     try:
#         data=[]
#         a=0
#         fig = plt.figure(figsize=(2,2),dpi=200)
#         ax = fig.add_subplot(1,1,1)
#         values=df["LICENSE"].value_counts()
#         ax.bar([x for x in range(len(values.index.to_list()))],values)
#         ax.set_xticks([x for x in range(len(values.index.to_list()))])
#         ax.set_xticklabels(values.index.to_list())
#
#
#         plt.show()
#     except Exception as e:
#         print(e)


def returnTypes():
    return [("콘텐츠 기반 워드 클라우드 보기",process),
            ("타이틀 기반 워드 클라우드 보기",process2),
            # ("링크 출처 통계 보기",process3),
            # ("라이선스 통계 보기", process4)
            ]
