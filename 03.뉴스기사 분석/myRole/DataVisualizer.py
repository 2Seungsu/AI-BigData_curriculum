from	bs4	import	BeautifulSoup 
import	requests
from	konlpy.tag import	Okt
from	collections	import	Counter
from	wordcloud import	WordCloud
import	matplotlib.pyplot as	plt
import	time
import	re
import	platform

#시각화
from plotnine import *
from matplotlib import font_manager, rc
#폰트
font_name= font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family = font_name)

import pandas as pd

def returnTypes():
    return [("추이 그래프 보기",process)]

#process(pd.read_csv("ai_critize.csv",encoding="UTF-8",header=0))
def	make_wordcloud(word_count,	title_list): 
    okt =	Okt()
    sentences_tag =	[]
    #	형태소 분석하여 리스트에 넣기 
    for	sentence	in	title_list:
        morph	=	okt.pos(sentence) 
        sentences_tag.append(morph) 
    #    print(morph)
    #    print('-'	*	30) 
    #print(sentences_tag)
    #print('\n'	*	3) 
    noun_adj_list =	[]
    
    #	명사와 형용사만 구분하여 이스트에 넣기 
    for	sentence1	in	sentences_tag:
        for	word,	tag	in	sentence1:
            if	tag	in	['Noun'] and word not in ['수','것','등','생','이','를','고','의','엑사','그']: 
                noun_adj_list.append(word)
    #형태소별 count
    counts	=	Counter(noun_adj_list)
    tags	=	counts.most_common(word_count) 
    #print(tags)

    #	wordCloud생성
    #	한글 꺠지는 문제 해결하기위해 font_path 지정 
    if	platform.system()	==	'Windows':
        path	=	r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system()	==	'Darwin':		#	Mac	OS 
        path	=	r'/System/Library/Fonts/AppleGothic'
    else:
        path	=	r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

    dic = dict(tags)

    wc = WordCloud(font_path=path, background_color='white',	width=800,	height=600) 
    print(dic)

    cloud = wc.generate_from_frequencies(dic)
    plt.figure(figsize=(10,	8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

    return dic
#make_wordcloud(10,ndf['CONTENT'].to_list())


ai_critize = pd.read_csv('ai_critize.csv')
ai_critize = ai_critize.rename(columns={'Header':'TITLE','Link':'URL','Content':'CONTENT'})
ai_document = pd.read_csv('ai_document.csv')
ai_document = ai_document.rename(columns={'Header':'TITLE','Link':'URL','Content':'CONTENT'})
ai_report = pd.read_csv('ai_report.csv')
ai_report = ai_report.rename(columns={'Header':'TITLE','Link':'URL','Content':'CONTENT'})


#df[["URL","TITLE","CONTENT","LICENSE"]]
def process(df):
    ac = make_wordcloud(15,ai_critize['CONTENT'].to_list())
    ad = make_wordcloud(15,ai_document['CONTENT'].to_list())
    ar = make_wordcloud(15,ai_report['CONTENT'].to_list())

    ndf1 = pd.DataFrame([ac]).T
    ndf1['분야'] = '논문'
    ndf2 = pd.DataFrame([ad]).T
    ndf2['분야'] = '문서'
    ndf3 = pd.DataFrame([ar]).T
    ndf3['분야'] = '보고서'

    ndf = pd.concat([ndf1,ndf2,ndf3])
    ndf['분야'] = ndf['분야'].astype('category')

    p1 = ggplot(ndf) + geom_bar(aes(x=ndf.index,y=ndf[0],color = ndf['분야'],fill = ndf['분야']),stat='identity') + theme(text=element_text(fontproperties=font_name),axis_text_x=element_text(angle=60, hjust=1))  
    print(p1)

process(None)




