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

import time

import pandas as pd

from Jinho.ASiteCralwer import ASiteCralwer
from Jinho.Logger import Logger
from Jinho.WebDriver import WebDriver
from Jinho.InnerSiteCralwer import SiteCralwer
log = Logger("connection.txt")

webDriver = WebDriver()
webDriver.initCrawling()

postCralwer = SiteCralwer(webDriver)
cral = ASiteCralwer(webDriver)

def getLink(year,maxPage,progress):

    link_all=[]
    searchs=["인공 지능 음악","AI 음악"]
    _max = maxPage * len(searchs)
    _nowValue=0
    print("작업을 수행합니다...")
    for i in range(maxPage):
        for x in searchs:
            links = cral.getItemsFromG("여기에 포털사이트 검색링크(수집시에만 사용) " + str(x)+f"&start={i*10}")

            link_all.extend(links)
            print(len(link_all))
            _nowValue +=1
            progress(_nowValue,_max)

        print("총 링크 " + str(len(link_all)) + "개")

    return link_all


def process(fileName,link_all,progress):

    endItems=[]
    a=0
    _nowValue=0
    _max = len(link_all)

    for i in link_all:
        a+=1
        try:
            print(i,"접속 시도...")
            it = postCralwer.getCrawling(i[1])

            endItems.append((i[1], it[1], i[0], it[0]))

            print(it)
            print(a , "/ " , len(link_all))
        except:
            print("ERR!")
        _nowValue +=1
        progress(_nowValue,_max)


    df = pd.DataFrame(endItems ,columns=["URL","LICENSE","TITLE","CONTENT"])
    print(df)
    df.to_csv(fileName +".csv",encoding="UTF-8",sep="|")