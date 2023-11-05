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

from bs4 import BeautifulSoup
import re

class SiteCralwer:
    def __init__(self, webDriver):
        self.__webDriver = webDriver
        self.__tagInfo ={}
        self.__tagInfo.update({"tistory.":[["entry-content","area-view","content",".*content.*"],"span.bundle_ccl"]})

    def _deleteErrors(self, text):
        text=text.replace("\n"," ")
        cmp=  re.compile("[a-zA-Z]|[\\<\\>\\(\\)\\*\\&\\^\\%\\$\\#\\@\\!\\~\"'\n]|[\\[\\]\\|\\;\\.\\,\\=\\{\\}\\+\\-]|\xa0|\t")
        cmp=cmp.sub("",text).strip()

        return cmp

    def _getSiteType(self,url):
        siteURL = re.match("https{0,1}://([^/]*)/{0,1}.*",url).groups()[0]

        for x in self.__tagInfo.keys():
            if(x in siteURL):
                return x
        return None



    def getCrawling(self, url):
        siteType = self._getSiteType(url)
        if(siteType==None):
            return None
        crawlOptions = self.__tagInfo[siteType]
        webDriver = self.__webDriver

        crawlTypes = crawlOptions[0]
        crawlCCL = crawlOptions[1]

        webDriver.moveSite(url)
        html = webDriver.getPageSource()

        bs = BeautifulSoup(html,"html.parser")
        items=[]

        license = bs.select_one(crawlCCL)
        if(license==None):
            license=""
            return ("","DENY")
        else:
            license= self._deleteErrors(license.get_text())


        for crawlType in crawlTypes:
            regex = re.compile(crawlType)

            ntd = bs.find_all("div",attrs={"class":regex})
            if(ntd!=None): items.extend(ntd)
            ntd = bs.find_all("div",attrs={"id":regex})
            if(ntd!=None): items.extend(ntd)


        selectedItem=""

        for item in items:
            if(item ==None or len(item)==0):
               continue
            txt = self._deleteErrors(item.text)
            if(selectedItem==""):
                selectedItem=txt

            if(len(txt)<=len(selectedItem)):
                selectedItem=txt
            break
            #print("==> " , txt)

        #print(selectedItem.text)

        return selectedItem.replace("  "," "), license

