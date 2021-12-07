# request 模块为原生网络模块，简单便捷，效率极高
# 作用是 模拟浏览器发送请求

# 1. 指定url: url = "...."    
# 2. 发送请求,并得到一个响应对象： response = requests.get(url)
# 3. 获取响应数据，通过调用响应对象的text属性，返回响应对象中储存的字符串： page_text = response.text
# 4. 持久化储存：with open('./xxx.com.html', 'w', encoding='UTF-8') as fp: fp.write(page_text)

import requests

if __name__ == "__main__":
    url = 'https://www.sogou.com/'
    response = requests.get(url=url)
    page_text = response.text
    with open('./sogou.html', 'w', encoding='UTF-8') as fp:
        fp.write(page_text)
    