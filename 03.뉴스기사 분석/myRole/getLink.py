import mynews
import pandas as pd

def getLinks(year,page,progress):

    _max = page
    nowValue=0

    result = []
    for n in range(page):
        #[(타이틀1,타이틀2),(링크1,링크2)]
        #[(타이틀1,링크1),(타이틀2,링크2)]
        Header, Link =mynews.newsL(f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=ai%20%EB%AC%B8%EC%84%9C&sort=0&photo=3&field=0&pd=0&ds=&de=&cluster_rank=28&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={10*n+1}')
        result.append((Header,Link))
        #[("타이틀","url"),(..)]
        nowValue+=1
        progress(nowValue, _max)
    
    results=[]
    for n in range(len(Header)):
        _header = Header[n]
        _url = Link[n]
        results.append((_header,_url))
    return results


def process(fileName,links, progress):
    result=[]
    _max = len(links)
    nowValue=0

    for x in links:
        _title = x[0]
        _url = x[1]      
        Content = mynews.cont_single(_url)
        result.append([_title,_url,Content])
        print(_title, _url, Content)

        nowValue+=1
        progress(nowValue, _max)

        


    df = pd.DataFrame(result)
    df.to_csv(fileName,index=False,encoding='utf-8',header=['TITLE','URL','CONTENT'])


def progress(value, max):
    print(value,"/",max)

links = getLinks(0,1,progress)
print(links)


process("test.csv",links,progress)
#print(result)

# Header, Link=mynews.newsL(f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=ai%20%EC%B0%BD%EC%9E%91%EB%AC%BC&sort=0&photo=3&field=0&pd=0&ds=&de=&cluster_rank=20&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={51}')
# Content = mynews.cont(Link)
# result=[]
# result.extend(list(zip(Header,Link,Content)))
# print(result)


#csv별 키워드 갯수 비교? 그래프? 공통 키워드?
#상위 5개뽑아서 csv별 시각화하면 잘보이지 않을까?

