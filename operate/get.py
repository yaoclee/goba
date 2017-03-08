#coding=gbk
import urllib
import urllib2
import requests
from lxml import etree

#url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.27.BCFq2r&id=39877056030&ns=1&abbucket=14&sku_properties=5919063:6536025"
#url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.27.mdvhY0&id=541675624149&ns=1&abbucket=14&sku_properties=5919063:6536025;12304035:3222911;122216431:27772"
url = "https://item.taobao.com/item.htm?spm=a230r.1.14.150.mdvhY0&id=543630918915&ns=1&abbucket=14#detail"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}

try:
    #request = urllib2.Request(url, headers=headers)
    #response = urllib2.urlopen(request)
    #str = response.read()
    
    str = requests.get(url, headers=headers)
    str.encoding = 'GBK'
    selector = etree.HTML(str.text)
    #nodes = selector.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1/a/text()')
    nodes = selector.xpath('//title/text()')

    for node in nodes:
        print node
        
    print nodes[0]
        
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason