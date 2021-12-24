from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 强制等待
def practice01():
    driver = webdriver.Chrome('./chromedriver') # 指定selenium使用chromedriver操作chrome解析网页

    # webdriver.Phantomjs('./phantomjs') # 如果使用phantomjs

    driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
    time.sleep(5)
    html = driver.page_source
    print(html)

# 智能等待
def practice02():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
    # text_to_be_present_in_element 某个元素的text里面出现了某些文本
    # presence_of_element_located 某个元素出现
    try:
        WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '通关'))
    except Exception as _:
        print('网页加载太慢了，不想等了。')

    element = driver.find_element_by_xpath('//div[@class="content"]')
    print(f'异步加载内容是：{element.text}')
    driver.quit()

practice02()


from selenium.webdriver.common.keys import Keys
def practice03():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.zhihu.com/#signin')
    elem = driver.find_element_by_name("account")
    elem.clear()
    elem.send_keys("xxx@163.com")
    password = driver.find_element_by_name('password')
    password.clear()
    password.send_keys('123456')
    input('请在网页上点击倒立的文字，完成以后回到这里按任意键继续。')
    elem.send_keys(Keys.RETURN) # 模拟键盘回车键