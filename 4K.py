import requests
from lxml import etree
import os

if __name__== "__main__":
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    url = 'http://pic.netbian.com/4kmeinv/'
    response = requests.get(url = url, headers=headers)
    #response.encoding = 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        img_data = requests.get(url=img_src,headers=headers).content
        image = 'picLibs/' + img_name
        with open(image, 'wb') as fp:
            fp.write(img_data)