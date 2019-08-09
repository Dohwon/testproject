# Crawler_daumblog.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def DaumBlogCrawler(keyword,Startdate,Enddate):
    dates_result = []
    titles_result = []
    summary_result = []
    for i in range(1, 100):
        p_url = 'http://search.daum.net/search?q=' + str(keyword) + '&w=blog&m=board&f=section&SA=daumsec&DA=PGD&lpp=10&nil_src=blog&page=' + str(i) + '&period=w&sd=' + str(Startdate) + '000000&ed=' + str(Enddate) + '235959'
        temp_result = requests.get(p_url)
        soup = BeautifulSoup(temp_result.text, 'html.parser')

        dates = soup.select('span.f_nb')
        titles = soup.select('a.f_link_b')
        texts = soup.select('p.f_eb')

        for tag, tag2, tag3 in zip(dates, titles, texts):
            dates_result.append(tag.text)
            titles_result.append(tag2.text)
            summary_result.append(tag3.text)

            my_dict = {'date':dates_result ,'title':titles_result , 'content':summary_result}
            df = pd.DataFrame(my_dict)
            df = df.drop_duplicates()

    return print(df)

#DaumBlogCrawler('서주혁','20190701','20190801')