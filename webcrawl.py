import requests

# User agent 伪装

if __name__ == "__main__":
    url = 'https://www.sogou.com/web'
    #处理url携带参数
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    kw = input('entere a word: ')
    param = {'query' : kw}
    response = requests.get(url = url, params = param, headers = headers)
    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='UTF-8') as fp:
        fp.write(page_text)