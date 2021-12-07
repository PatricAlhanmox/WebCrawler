'''
    - xpath解析原理：
        1. 实例化一个etree的对象，且需要将被查询的页面的源码加载到该对象中
        2. 调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获
    
    - 如何实例化etree对象：
        1. 将本地的html文档中的源码加载到etree对象中：etree.prase(filePath)
        2. 可以将从互联网上获取的源码数据加载到该对象中：etree.HTML('page_text')
        3. xpath('xpath表达式')
'''

    #instance the object
    # tree = etree.parse('test.html')
    # r = tree.xpath('/html/body/title')
    # r = tree.xpath('/html//div')
    # r = tree.xpath('//div')
    # r = tree.xpath('//div[@class_="song"]')
    # r = tree.xpath('//div[@class="song"]//li[5]/a/text()')[0]
    # r = tree.xpath('//div[@class="song"]/img/@src')

'''
        xpath表达式中的 / 从根节点开始定位。表示的是一个层级
        xpath表达式中的 // 多个层级。可以从任意位置省略中间的层级
        xpath表达式中的属性定位：//div[@class='XX'] tag[@attrName="attrVal"]
        xpath表达式中的索引定位：//div[@class='XX']/p[3] 注索引从1开始
        xpath取文本是用text()，当获取的文本不为父标签的直系子标签则将带上 ‘//’
        xpath取属性需要/@attrName
'''
import requests
from lxml import etree

if __name__ == "__main":
    url = 'https://bj.58.com/ershoufang/'
    headers = {'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML()
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('58.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.xpath('./li/div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')
