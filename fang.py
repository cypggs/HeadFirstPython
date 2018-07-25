# -*- coding: utf8 -*-
import  requests
import  bs4

def get_lastdata():
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
   }

   data = requests.get("http://zu.tj.fang.com/house/n31/", headers=headers)
   #因为打印出来的格式有乱码，所以更改一下编码
   data.encoding="gbk"
   soup = bs4.BeautifulSoup(data.text, "html.parser")
   # 标题
   title = soup.find_all("p", "title")
   # 价格
   price = soup.select("#listBox > div.houseList > dl > dd > div.moreInfo > p > span")
   # 具体的内容
   concretedata = soup.select("#listBox > div.houseList > dl > dd > p.font16.mt20.bold")

   for title,price,concretedata in zip(title,price,concretedata):
       last_data={
           "title":title.get_text().strip(),
           "concretedata":concretedata.get_text().strip(),
           "price":price.get_text().strip()
       }

       print(   last_data)

if __name__ == '__main__':
   get_lastdata()
