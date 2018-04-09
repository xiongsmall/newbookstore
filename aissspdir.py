import requests
from urllib import request
import gzip
import re
import os
from bs4 import BeautifulSoup
from threading import Thread,Lock
from time import sleep
mutex = Lock()
# header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
#         "referer": "https://www.meitulu.com/t/aiss/"
#     }
# url = 'https://mtl.ttsqgs.com/images/img/8782/18.jpg'
# req = request.Request(url,headers=header)
# req = request.urlopen(req)
# con = req.read()
# coding = req.headers.get('Content-Encoding')
# if coding == 'gzip':
#     con = gzip.decompress(con)
# f = open('/home/xionghao/workfiles/sisi/1.jpg','wb')
# f.write(con)
# f.close()
# print(con)
# url = 'https://www.meitulu.com/t/aiss/'

# req = requests.get(url,headers=header)
# con = req.text
# print(con)

# req = request.Request(url,headers=header)
# req = request.urlopen(req)
# con = req.read()
# con = gzip.decompress(con)
# con = con.decode('utf-8')
# bf = BeautifulSoup(con,'html5lib')
# # print(bf)
# bf_img = bf.find_all('a',class_="a1")
# for a in bf_img:
#     if a.text == '下一页':
#         print(a.attrs['href'])

# tn = re.findall(r'<div class="boxs">.*?</div>',con,re.S)
# tn = tn[0]
# bf_img = BeautifulSoup(tn,'html5lib')
# hreflist = bf_img.find_all('a')
# for i in hreflist:
#     href = i.attrs['href']
#     if href.endswith('html'):
#         print(href)

outimglist =[]
img_url =[]
class Geturl(object):
    def __init__(self,header):
        self.header = header

    def startouturl(self,url):
        if len(outimglist)>15: sleep(300);print(outimglist)
        req = request.Request(url,headers=self.header)
        req = request.urlopen(req)
        con = req.read()
        coding = req.headers.get('Content-Encoding')
        if coding == 'gzip':
            con = gzip.decompress(con)
        con = con.decode('utf-8')
        self.getouturl(con)
        self.getoutnext(con)

    def getouturl(self,con):
        tn = re.findall(r'<div class="boxs">.*?</div>', con, re.S)
        tn = tn[0]
        bf_img = BeautifulSoup(tn,'html5lib')
        hreflist = bf_img.find_all('a')
        for i in hreflist:
            href = i.attrs['href']
            if href.endswith('html'):
                if href in outimglist:
                    pass
                else:
                    outimglist.append(href)

    def getoutnext(self,con):
        bf = BeautifulSoup(con, 'html5lib')
        bf_img = bf.find_all('a', class_="a1")
        if bf_img:
            for a in bf_img:
                if a.text == '下一页':
                    href = a.attrs['href']
                    href ='https://www.meitulu.com'+href
                    sleep(1)
                    self.startouturl(href)

class Getinurl(object):
    def __init__(self,header):
        self.header = header
        self.src = None

    def starturl(self,href=None):
        # print(img_url)
        if href==None:
            if outimglist:
                if len(img_url)>15: sleep(15);print(img_url)
                href = outimglist[0]
                print(11111)
                print(outimglist)
                del outimglist[0]
                print(2222222)
                print(outimglist)
                req = request.Request(href, headers=self.header)
                req = request.urlopen(req)
                con = req.read()
                coding = req.headers.get('Content-Encoding')
                if coding == 'gzip':
                    con = gzip.decompress(con)
                con = con.decode('utf-8')
                self.armurl(con)
                self.nexturl(con)
            else:
                sleep(5)
                self.starturl()
        else:
            req = request.Request(href,headers=self.header)
            req = request.urlopen(req)
            con = req.read()
            coding = req.headers.get('Content-Encoding')
            if coding == 'gzip':
                con = gzip.decompress(con)
            con = con.decode('utf-8')
            self.armurl(con)
            self.nexturl(con)



    def armurl(self,con):
        bf = BeautifulSoup(con,'lxml')
        bf_img = bf.find('center')
        img = bf_img.find_all('img')
        for i in img:
            img_u = i.attrs['src']
            img_url.append(img_u)

    def nexturl(self,con):
        bf = BeautifulSoup(con,'lxml')
        bf_img = bf.find_all('a', class_="a1")
        if bf_img:
            for a in bf_img:
                if a.text == '下一页':
                    href1 = a.attrs['href']
                    if href1 == self.src:
                        self.src = None
                        self.starturl(href=None)
                    else:
                        self.src =href1
                        href ='https://www.meitulu.com'+href1
                        self.starturl(href=href)

class saveimg(object):
    def __init__(self,header):
        self.num = 0
        self.header = header
    def writeimg(self,con):
        if os.path.exists('/home/xionghao/sisi'):
            mutex.acquire()
            self.num = self.num + 1
            f = open('/home/xionghao/sisi/'+str(self.num)+'.jpg','wb')
            f.write(con)
            print('成功下载%s张'%self.num)
            f.close()
            mutex.release()
            self.readurl()
        else:
            os.makedirs('/home/xionghao/sisi')
            self.writeimg(con)
    def readurl(self):
        if img_url:
            print(11111)
            mutex.acquire()
            href = img_url[0]
            del img_url[0]
            mutex.release()
            try:
                req = request.Request(href,headers=self.header)
                req = request.urlopen(req)
                con = req.read()
                self.writeimg(con)
            except Exception as e:
                print(e)
                print(22222)
                self.readurl()
        else:
            sleep(10)
            self.readurl()


if __name__ =='__main__':
    # pass
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        "referer": "https://www.meitulu.com/t/aiss/"}
    url = 'https://www.meitulu.com/t/aiss/'
    g1 = Geturl(header)
    g2 = Getinurl(header)
    g3 = saveimg(header)
    t1 = Thread(target=g1.startouturl,args=(url,))
    t2 = Thread(target=g2.starturl,)
    t3 = Thread(target=g3.readurl,)
    t4 = Thread(target=g3.readurl,)
    t5 = Thread(target=g3.readurl,)
    t6 = Thread(target=g3.readurl,)
    t7 = Thread(target=g3.readurl,)
    t8 = Thread(target=g3.readurl,)
    t9 = Thread(target=g3.readurl,)
    t10 = Thread(target=g3.readurl,)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
