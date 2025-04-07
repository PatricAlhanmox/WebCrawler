from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, requests


if __name__ == "__main__":
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        "Accept-Language": "zh-CN,zh;q=0.9"
    
    }
    url = "https://fsop.caac.gov.cn/yzzzm/view/WebDesktop/login.jsp"
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
    input_username = browsers.find_element(By.NAME, value="loginName")
    input_username.send_keys('210106198409154371')
    time.sleep(2)
    input_password = browsers.find_element(By.NAME, value="password")
    input_password.send_keys('Shy!840915')
    time.sleep(1)

    input_valid = input("输下验证码： ")
    validation = browsers.find_element(By.NAME, value="image_uf")
    validation.send_keys(input_valid)
    time.sleep(4)
    
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-key")))
    button.click()

    time.sleep(15)