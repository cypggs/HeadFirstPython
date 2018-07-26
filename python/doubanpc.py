#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os, socket

class Spider:
    def __init__(self, url='https://movie.douban.com/top250'):
        self.url = url
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }

    #生成目录
    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\mdouban", path))
        if not isExists:
            os.makedirs(os.path.join("D:\mdouban", path))
            os.chdir(os.path.join("D:\mdouban", path))
        else:
            os.chdir(os.path.join("D:\mdouban", path))
        return os.path.abspath('.')

    #获取BeautifulSoup
    def get_soup(self, link):
        html = requests.get(link, headers=self.header)
        html.encoding = html.apparent_encoding
        soup = BeautifulSoup(html.text, 'lxml')
        return soup


if __name__ == '__main__':
    socket.setdefaulttimeout(20)
    spider = Spider()
    path = spider.mkdir('top250')
    print('starting get data from douban...')
    f = open(path+'/top.txt', 'a', encoding='utf-8')
    #outputMode = "{0:^15}\t{1:^9}\t{2:^15}\t{3:^30}" 设置输出格式，直接print显示效果还可以，可是输出到text里显示就完全不行了，不知道为什么
    f.write('排名     电影名称                评分      评论人数            短评                              \n')

    #top250共十页
    for i in range(1, 11):
        if i == 1:
            url = spider.url
        else:
            url = spider.url + '?start=' + str(25*(i-1)) + '&filter='   #后面9页的链接需要拼接
        main_soup = spider.get_soup(url)
        ol_grid = main_soup.find('ol', class_='grid_view')
        li = ol_grid.find_all('li')
        for l in li:
            item = []
            em_rank = l.find('em').get_text()
            item.append(em_rank)

            div_hd = l.find('div', class_='hd')
            a = div_hd.find('a')
            title = a.find('span', class_='title').get_text()
            item.append(title)

            div_star = l.find('div', class_='star')
            rating_num = div_star.find('span', class_='rating_num').get_text()
            item.append(rating_num)
            review = div_star.find_all('span')[3].get_text()
            item.append(review)

            div_bd = l.find('div', class_='bd')
            q = div_bd.find('span', class_='inq')
            if q != None:   #部分电影是没有短评的，所以需要判断
                quote = q.get_text()
                item.append(quote)
            else:
                item.append('无')
            f.write(item[0]+'     '+item[1]+'                '+item[2]+'      '+item[3]+'            '+item[4]+ '                              \n')
    f.close()
    print('over!')
