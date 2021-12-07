import requests

if __name__ == '__main__':
    canteen = input('Enter restruant: ')
    param = {
        'cname' : '',
        'pid' : '',
        'keyword' : canteen,
        'pageIndex' : '1',
        'pageSize' : '10',
    }
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    response = requests.post(url = url, params = param, headers = ua)
    info = response.text
    fileName = canteen + '.text'
    with open(fileName, 'w', encoding='UTF-8') as fp:
        fp.write(info)