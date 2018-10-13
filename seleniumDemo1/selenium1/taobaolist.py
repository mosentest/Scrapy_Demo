from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 900)
    driver.get(
        "https://s.taobao.com/list?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&spm=a219r.lmn002.1000187.1&style=list")
    print("wwww")
    time.sleep(4)
    print("wwww2222")
    # driver.
    elem = driver.find_elements_by_xpath('//div[@class="wraper"]/div/ul/li')
    print(elem)
    i = 0
    for x in elem:
        if(i>1):
            x.click()
            time.sleep(10)
            break
        i=i+1
    # driver.close()
finally:
    # driver.close()
    pass
