#目标是爬取三国演义小说里的所有标题和章节
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).text

    #1.initialise the beauitfulsoup object
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu > ul > li')

    fp = open('./sanguo.text', 'w', encoding='UTF-8')

    for li in li_list:
        title = li.a.string 
        detail_url = 'http://www.shicimingju.com' + li.a['href']
        detail_page = requests.get(headers=headers,url=detail_url).text
        soup1 = BeautifulSoup(detail_page, 'lxml')
        div_tag = soup1.find('div', class_='chapter_content')
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
