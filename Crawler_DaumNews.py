# Crawler_daumnews.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def DaumNewsCrawler(date):
    company_result = []
    titles_result = []
    summary_result = []
    category_result = []
    categories = {'사회':'society','정치':'politics','경제':'economic','국제':'foreign','문화':'culture','연예':'entertain','스포츠':'sports','IT':'digital','칼럼':'editorial','보도자료':'press'}
    #category1 = categories.get(category)
    for news in categories.values():
        url = 'https://media.daum.net/breakingnews/' + str(news) +'&regDate=' +str(date)
        #url_result = requests.get(url)
        #soup = BeautifulSoup(url_result.text,'html.parser')
        for i in range(1, 3):
            p_url = str(url) + '&page=' + str(i)
            temp_result = requests.get(p_url)
            soup = BeautifulSoup(temp_result.text, 'html.parser')

            company = soup.select('span.info_news')
            titles = soup.select('a.link_txt')
            texts = soup.select('span.link_txt')

            for tag, tag2, tag3 in zip(company, titles, texts):
                company_result.append(tag.text)
                titles_result.append(tag2.text)
                summary_result.append(tag3.text)
                category_result.append(news)

                my_dict = {'date':date, 'category':category_result,'company':company_result ,'title':titles_result , 'content':summary_result}
                df = pd.DataFrame(my_dict)
                df = df.drop_duplicates()

    return print(df)

DaumNewsCrawler('20190808')