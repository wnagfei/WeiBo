from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
import time
def selenuim_loading_more(browser, method_index=0):
    if method_index==0:
        browser.implicitly_wait(3) # 为了快速滑动，先设置超时时间为1秒
        # while True:
        for i in range(1, 4): # at most 3 times
            print ("loading more, window.scrollTo bettom for the", i,"time ...")
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            try:
                # 定位页面底部的换页tab
                browser.find_element_by_css_selector("div[class='W_pages']")
                break # 如果没抛出异常就说明找到了底部标志，跳出循环
            except NoSuchElementException:
                pass # 抛出异常说明没找到底部标志，继续向下滑动
        browser.implicitly_wait(4) # 将超时时间改回10秒
    elif method_index==1:
        browser.find_element_by_css_selector("div[class='empty_con clearfix']").click() # loading more
        print ("loading more, sleep 4 seconds ... 1")
        time.sleep(4)
        browser.find_element_by_css_selector("div[class='empty_con clearfix']").click() # loading more
        print ("loading more, sleep 3 seconds ... 2")
        time.sleep(2)
    elif method_index==2:
        load_more_1 = browser.find_element_by_css_selector("div[class='empty_con clearfix']") # loading more
        ActionChains(browser).click(load_more_1).perform()
        print ("loading more, sleep 4 seconds ... 1")
        time.sleep(4)
        load_more_2 = browser.find_element_by_css_selector("div[class='empty_con clearfix']") # loading more
        ActionChains(browser).click(load_more_2).perform()
        print ("loading more, sleep 3 seconds ... 2")
        time.sleep(2)
    elif method_index==3:
        print ("loading more, sleep 4 seconds ... 1")
        element = WebDriverWait(browser, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='empty_con clearfix']"))
        )
        element.click()
        print ("loading more, sleep 2 seconds ... 2")
        WebDriverWait(browser, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='empty_con clearfix']"))
        ).click()
    return browser
