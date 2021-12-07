import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    param = {
        'type' : '24',
        'interval_id' : '100:90',
        'action' : '',
        'start' : '0',
        'limit': '1',
    }
    responds = requests.get(url = url, params=param, headers=ua)
    fileName = 'Douban.json'
    dic = responds.json()
    json.dump(dic, fp=open(fileName, 'w', encoding='UTF-8'), ensure_ascii=False)