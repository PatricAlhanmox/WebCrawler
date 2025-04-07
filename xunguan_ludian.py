from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from queue import Queue
import time, requests


if __name__ == "__main__":
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        "Accept-Language": "zh-CN,zh;q=0.9"
    
    }
    url = "http://fms.cafuc.edu.cn/login.html"
    #模拟登陆
    options = webdriver.ChromeOptions()

    #处理证书
    options.add_argument('--ignore-certificates-errors')
    options.add_experimental_option("excludeSwitches",['enable-automation'])
    options.add_argument("--disable-blink-features=AutomationControlled")
    chromedriver_path = Service(r"D:\python\Scripts\chromedriver.exe")

    browsers = webdriver.Chrome(options=options, service=chromedriver_path)
    browsers.get(url)
    wait = WebDriverWait(browsers, 10)

    # 模拟登陆
    input_username = browsers.find_element(By.NAME, value="j_username")
    input_username.send_keys('513128199312056018')
    time.sleep(2)
    input_password = browsers.find_element(By.NAME, value="j_password")
    input_password.send_keys('Zx19931205!')
    time.sleep(1)
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "login_button")))
    button.click()

    # 进入页面后获取cookies
    cookies_raw = browsers.get_cookies()
    cookies = {}
    for ck in cookies_raw:
        for item in ck.items():
            cookies[str(item[0])] = str(item[1])
    cookies[cookies["name"]] = cookies["value"]
    del cookies["name"]
    del cookies["value"]

    # 获取主页面
    response = requests.get("https://fms.cafuc.edu.cn/layout.html", headers=headers, cookies=cookies)
    #模拟点击训练管理 ==>> 课程训练记录 ==>> 具体记录
    elements_trainmanage = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "navLi_a")))
    elements_trainmanage[3].click()
    time.sleep(1.5)

    # 课程训练记录 
    left_item = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='left']")))
    train_rec_outter = left_item.find_element(By.LINK_TEXT, "课程训练记录")
    train_rec_outter.click()
    time.sleep(1)

    # 具体记录
    inner_items = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='管理课程训练记录']")))
    time.sleep(1)
    inner_items.click()
    time.sleep(20)


    # 获取训管页面
    trainmanage_params = {
        "menuId": "TOP-TRAIN-ID"
    }
    train_manage_page = requests.get(url=url, 
                                     params=trainmanage_params, 
                                     headers=headers, 
                                     cookies=cookies,
                                     timeout=10,
                                     verify=True)
    train_manage_page.raise_for_status()  # 自动处理4xx/5xx错误
    # 处理响应内容
    print(f"响应状态码: {train_manage_page.status_code}")
    print(f"实际请求URL: {train_manage_page.url}")
    
    
    #获取子页面
    iframe_locator = (By.CLASS_NAME, "index_iframe")
    try:
        wait.until(
                EC.frame_to_be_available_and_switch_to_it(iframe_locator)
            )
        print("成功切换到iframe上下文")
    except:
        print("iframe处理失败")
    #进行翻页
    page_box= browsers.find_element(By.CLASS_NAME, "page_box")
    pages = []
    for item in page_box.find_elements(By.TAG_NAME, "li"):
        pages.append(item.text)
    del pages[0:2]
    q = Queue(maxsize=len(pages))

    # 获取每行数据
    for p in pages:
        iframe_html = browsers.page_source
        print(p)
        page_box= browsers.find_element(By.CLASS_NAME, "page_box")
        page_href = page_box.find_elements(By.LINK_TEXT, p)
        if len(page_href) != 0:
            page_href[0].click()
        time.sleep(1)
        rows = browsers.find_elements(By.CLASS_NAME, "xfy_table tbody")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "tr")
            del cells[0]
            row_data = [cell.text for cell in cells]
            print(row_data)
        time.sleep(1)

        

        '''
        if p != pages[-1]:
            next_page_button = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "li")))
            next_page_button[int(p)+1].click()
        '''
        wait
    
    browsers.close()
