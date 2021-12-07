import requests
import json

# 没查找一个单词都是一个字符串发送了ajax请求（POST）/ 响应数据是一组josn数据

if __name__ == "__main__":
    url = 'https://fanyi.baidu.com/sug'
    ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    word = input("enter a word: ")
    param = {
        'kw' : word
    }
    respond = requests.post(url = url, data = param, headers = ua)
    fileName = word + '.json'
    dic = respond.json()
    json.dump(dic, fp=open(fileName, 'w', encoding='UTF-8'), ensure_ascii=False)