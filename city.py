from lxml import etree
import requests
import os

if __name__ == '__main__':
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    url = 'https://www.aqistudy.cn/historydata'
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    all_city = []
    for li in li_list:
        city_name = li.xpath('./a/text()')[0]
        all_city.append(city_name)
    
    all_name = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in all_name:
        city_name = li.xpath('./a/text()')[0]
        all_city.append(city_name)
    
    if not os.path.exists('./cityName'):
        os.mkdir('./cityName')
    fileName = 'cityName'+'.txt'
    with open('cityName/'+fileName,'w',encoding='UTF-8') as fp:
        for na in all_city:
            fp.write(na + ' ')
