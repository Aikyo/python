
# import requests
# from lxml import html
# url='https://music.douban.com/' #需要爬的网址
# page=requests.Session().get(url)
# tree=html.fromstring(page.text)
# result=tree.xpath('//tr//a/text()') #需要获取的数据
# result1=tree.xpath('//tr//a/@href')
# result2=tree.xpath('//tr[last()]//a/@href')
# print(result)
# print(result1)


from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

url = "https://movie.douban.com/chart"
f = requests.get(url)                 #Get该网页从而获取该html内容
soup = BeautifulSoup(f.content, "lxml")  #用lxml解析器解析该网页的内容, 好像f.text也是返回的html
#print(f.content.decode())
#content = soup.find_all('div',class_="p12" )   #因为calss和关键字冲突，所以改名class_

for k in soup.find_all('div',class_='pl2'):#,找到div并且class为pl2的标签
   a = k.find_all('span')       #在每个对应div标签下找span标签，会发现，一个a里面有四组span
   print(a[0].string)
