#coding=utf-8
import urllib
import re


def getHtml(url):
    page = urllib.urlopen(url)
    return page.read()


def getImg(html):
    reg = r'src="(.+?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    for x, imgurl in enumerate(imglist):
        urllib.urlretrieve(imgurl, '%s.jpg' % (x, ))
    # return imglist


html = getHtml('http://python.jobbole.com/81359/')
getImg(html)

