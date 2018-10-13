from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 900)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    print("wwww")
    time.sleep(5)
    print("wwww2222")
    elem = driver.find_element_by_name('q')
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    # driver.close()
except:
    print("error")
finally:
    driver.close()
