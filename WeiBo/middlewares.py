# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
import time
class WeiboMiddleware():
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))
    def __init__(self, timeout=None, service_args=[]):
            self.logger = getLogger(__name__)
            self.timeout = timeout
            self.browser = webdriver.PhantomJS(service_args=service_args)
            self.browser.set_window_size(1400, 700)
            self.browser.set_page_load_timeout(self.timeout)
            self.wait = WebDriverWait(self.browser, self.timeout)
            self.js1 = "var q=document.documentElement.scrollTop=5000"
    def __del__(self):
            self.browser.close()

    def selenuim_loading_more(self,browser, method_index=0):
        if method_index == 0:
            browser.implicitly_wait(3)  # 为了快速滑动，先设置超时时间为1秒
            # while True:
            for i in range(1, 4):  # at most 3 times
                print("loading more, window.scrollTo bettom for the", i, "time ...")
                browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                try:
                    # 定位页面底部的换页tab
                    browser.find_element_by_css_selector("div[class='W_pages']")
                    break  # 如果没抛出异常就说明找到了底部标志，跳出循环
                except NoSuchElementException:
                    pass  # 抛出异常说明没找到底部标志，继续向下滑动
            browser.implicitly_wait(4)  # 将超时时间改回10秒
        elif method_index == 1:
            browser.find_element_by_css_selector("div[class='empty_con clearfix']").click()  # loading more
            print("loading more, sleep 4 seconds ... 1")
            time.sleep(4)
            browser.find_element_by_css_selector("div[class='empty_con clearfix']").click()  # loading more
            print("loading more, sleep 3 seconds ... 2")
            time.sleep(2)
        elif method_index == 2:
            load_more_1 = browser.find_element_by_css_selector("div[class='empty_con clearfix']")  # loading more
            ActionChains(browser).click(load_more_1).perform()
            print("loading more, sleep 4 seconds ... 1")
            time.sleep(4)
            load_more_2 = browser.find_element_by_css_selector("div[class='empty_con clearfix']")  # loading more
            ActionChains(browser).click(load_more_2).perform()
            print("loading more, sleep 3 seconds ... 2")
            time.sleep(2)
        elif method_index == 3:
            print("loading more, sleep 4 seconds ... 1")
            element = WebDriverWait(browser, 4).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='empty_con clearfix']"))
            )
            element.click()
            print("loading more, sleep 2 seconds ... 2")
            WebDriverWait(browser, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='empty_con clearfix']"))
            ).click()
        elif method_index == 4:
            print("loading more, sleep 2 seconds ... test")
            element = WebDriverWait(browser, 4).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='page next S_txt1 S_line1']"))
            )
            element.click()
            try:
                browser.find_element_by_xpath("//a[@class='page next S_txt1 S_line1']")
            except:
                NoSuchElementException("没有找到下一页或者已经到了最后一页")

        return browser
    def process_request(self, request, spider):
            """
            用PhantomJS抓取页面
            :param request: Request对象
            :param spider: Spider对象
            :return: HtmlResponse
            """
            self.logger.debug('PhantomJS is Starting')
            useSelenium = request.meta.get('useSelenium',False)
            try:
                if useSelenium:
                    self.browser.get(request.url)
                    print("loading more, sleep 3 seconds ... 0")
                    time.sleep(3)
                    browser = self.selenuim_loading_more(self.browser, method_index=0)

                    return HtmlResponse(url=request.url, body=browser.page_source, request=request,
                                        encoding='utf-8',
                                        status=200)
            except:
                 print("one exception happen ==> get_tweeter_under_topic  2  ...")
                 return HtmlResponse(url=request.url, status=500, request=request)
                 pass

