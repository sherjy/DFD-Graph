
# coding: utf-8

# In[95]:


# # import requests
# # from lxml import etree
# # import time
# # # for a in range(10):
# # #     url = 'https://book.douban.com/top250?start={}'.format(a*25)
# # #     data = requests.get(url).text
# # #     data = requests.get(url).text
# # #     s=etree.HTML(data)
# # #     file=s.xpath('//*[@id="content"]/div/div[1]/div/table') 

# # #     #print (file)
# # #     for div in file :
# # #         title = div.xpath("./tr/td[2]/div[1]/a/@title")[0]
# # #         score=div.xpath("./tr/td[2]/div[2]/span[2]/text()")[0] 
# # #         print("{} {}".format(title,score))
# # url= "http://cd.xiaozhu.com/"
# # data=requests.get(url).text
# # s=etree.HTML(data)
# # file=s.xpath('//*[@id="page_list"]/ul/li/div[2]/div/a/span/text()')
# # time.sleep(20)
# # for title in file:
# #     print (title)
# #-*- coding:utf-8 -*-
# from lxml import etree
# import requests
# import time

# with open('D:\\crawler\\xzzf.txt','w',encoding='utf-8') as f:
#     for a in range(1,6):
#         url = 'http://cd.xiaozhu.com/search-duanzufang-p{}-0/'.format(a)
#         data = requests.get(url).text

#         s=etree.HTML(data)
#         file=s.xpath('//*[@id="page_list"]/ul/li')
#         time.sleep(3)
    
#         for div in file:
#             title=div.xpath("./div[2]/div/a/span/text()")[0]
#             price=div.xpath("./div[2]/span[1]/i/text()")[0]
#             scrible=div.xpath("./div[2]/div/em/text()")[0].strip()
#             pic=div.xpath("./a/img/@lazy_src")[0]
#             print ("{},{},{},{}\n".format(title,price,scrible,pic)) 
#             f.write("{},{},{},{}\n".format(title,price,scrible,pic)) 
import requests
import json
import time

with open('D:\\crawler\\xzzf.txt','w',encoding='utf-8') as f:
    for a in range(3):
        url_visit = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}'.format(a*20)
        file = requests.get(url_visit).json()   #这里跟之前的不一样，因为返回的是 json 文件
        time.sleep(2)

        for i in range(20):
            dict=file['data'][i]   #取出字典中 'data' 下第 [i] 部电影的信息
            urlname=dict['url']
            title=dict['title']
            rate=dict['rate']
            cast=dict['casts']

            print('{}  {}  {}  {}\n'.format(title,rate,'  '.join(cast),urlname))
            f.write('{}  {}  {}  {}\n'.format(title,rate,'  '.join(cast),urlname))

