import requests
from bs4 import BeautifulSoup
import random
import time

#li = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=ai%20%EB%B3%B4%EA%B3%A0%EC%84%9C&sort=0&photo=3&field=0&pd=0&ds=&de=&cluster_rank=65&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1'

def newsL(link):
    #헤드라인 본문링크가져오기   
    html = requests.get(link).text
    soup = BeautifulSoup(html,'html.parser')

    #헤드라인
    newsHeader = []
    for i in soup.find_all(attrs={'class':'news_area'}):
        newsHeader.append(i.find_all('a')[5].text)
    #본문링크
    newsLink = []
    for i in soup.find_all(attrs={'class':'info_group'}):
        try:
            newsLink.append(i.find_all('a')[1]['href'])
        except Exception:
            continue

    return newsHeader,newsLink
#print(newsL(li))
#d = newsL(li)
#d[1]


def cont_single(url):
    #본문 들어가서 내용가져요기
    time.sleep(2+random.random())

    htmi = requests.get(url).text
    soui = BeautifulSoup(htmi,'html.parser')
    content = soui.select_one('#dic_area').text.replace('\n','').replace('\xa0','')

    
    return content


# def cont(linkList):
#     #본문 들어가서 내용가져요기
#     content = []
#     for i in linkList:
#         time.sleep(2+random.random())

#         htmi = requests.get(i).text
#         soui = BeautifulSoup(htmi,'html.parser')
#         content.append(soui.select_one('#dic_area').text.replace('\n','').replace('\xa0',''))

#     return content


#dd = cont(d[1])
#print(dd)
#ddd = list(zip(*d,dd))
#print(ddd)

# result = []
# for n in range(10):
#     Header, Link =newsL(f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=ai%20%EB%B3%B4%EA%B3%A0%EC%84%9C&sort=0&photo=3&field=0&pd=0&ds=&de=&cluster_rank=65&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={10*n+1}')
#     Content = cont(Link)

#     result.append(list(zip(Header,Link,Content)))

# print(result)

