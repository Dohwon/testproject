from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen

driver_path = '../resources/chromedriver' # driver path
base_url="https://search.shopping.naver.com/search/category.nhn?pagingIndex={}&pagingSize=40&viewType=list&sort=rel&cat_id=50000807&frm=NVSHPAG"

browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
chart_list=[]

for n in range(11):
    url=base_url.format(n+1)
    browser.get(url)
    webpage = urlopen(url)
    page = browser.page_source
    # browser.quit()

    soup = BeautifulSoup(webpage, 'html.parser')
    charts = soup.find_all('a', {'class': "tit"})   #same with findAll

    for chart in charts:
        chart_list.append(chart.get_text().strip().replace('\n', '').replace('\t', '').replace('\r', '').replace('쇼핑몰별 최저가','').split(' '))
browser.quit()

shopping_list=sum((chart_list),[])
shopping_list=str(shopping_list)
print(shopping_list)


file=open('shoppinglist.txt','w',encoding='utf=8')
for chart in shopping_list:

    file.write(chart)
file.close()


print(chart)
print(len(shopping_list))

from konlpy.tag import Hannanum
from collections import Counter
import pytagcloud  # Add fonts supporting Korean

f = open("../data_example/shoppinglist.txt", "r",encoding='UTF-8')
shoppinglist = f.read()

data={}
words=shoppinglist.split(',')
for w in words:
    if w in data:
        data[w]=data[w]+1
    else:
        data[w]=1
sorted_keys=sorted(data,key=data.get, reverse=True)
sorted_values=sorted(data.values(),reverse=True)
sorted_keys=sorted_keys[:100]
sorted_values=sorted_values[:100]
data_cloud={}
for i in range(len(sorted_keys)):
    k=sorted_keys[i]
    v=sorted_values[i]
    data_cloud[k]=v
print(data_cloud)

# h = Hannanum()
# nouns = h.nouns(shoppinglist)
# count = Counter(nouns)
# print(count)
#
# tag = count.most_common(500)
# tag_list = pytagcloud.make_tags(tag, maxsize=100)
tag_list = pytagcloud.make_tags(dict(data_cloud).items(), maxsize=100)
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(800,600), fontname='Korean',rectangular=False)

import webbrowser
webbrowser.open('word_cloud.jpg')