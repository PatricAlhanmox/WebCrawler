import requests
import json

if __name__ == '__main__':
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}


    l_id = []
    all_data = []
    url1 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    for page in range(1, 6):
        page = str(page)
        param1 = {
            'on' : 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname': '',
        }
        json_id = requests.post(url = url1, data = param1, headers=headers).json()

        for dic in json_id["list"]:
            l_id.append(dic["ID"])

    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    for i in l_id:
        param = {'id' : i}
        response_json = requests.post(url = url, params=param, headers = headers).json()
        all_data.append(response_json)
    json.dump(all_data, fp=open('zhuanli.json', 'w', encoding='UTF-8'), ensure_ascii=False)