# -*- coding: utf-8 -*-

# Scrapy settings for WeiBo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WeiBo'

SPIDER_MODULES = ['WeiBo.spiders']
NEWSPIDER_MODULE = 'WeiBo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'WeiBo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
  "Cookie": "SINAGLOBAL=8108552386944.921.1531462818774; un=18864233964; _s_tentry=www.google.com; Apache=6288455084085.116.1532421528936; ULV=1532421528991:3:3:2:6288455084085.116.1532421528936:1532310534552; login_sid_t=fa403ff4c7e1a495d31bf2acbbe6c720; cross_origin_proto=SSL; UOR=,,login.sina.com.cn; SCF=Av99oIep_6ZnthxvUCPbEeeGt7uFkJkRXgPQFhdGF3dm6_0rj5V-ppbRijy3UjPxCgV5KKftV_d--yc3hiwSSBA.; SUB=_2A252XEdXDeRhGeNI6lEW9y3LyT-IHXVVKD-frDV8PUNbmtAKLUPNkW9NSLWVV58W8pwCTsdXQ0kmLYsTUybMNjIg; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhTT7sxDJj3FgWrEqGDnY4f5JpX5K2hUgL.Fo-ceKeNS0eNeoe2dJLoIEXLxK-L1h-LBo5LxK-LBo5LB.eLxKqL1KqLB-qLxKML1h.LBo.LxK.LBKeL1--t; SUHB=0cSnV9UCWorLMt; ALF=1533112710; SSOLoginState=1532507911 ",
  "Accept-Encoding": "gzip, deflate, br"
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'WeiBo.middlewares.WeiboSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'WeiBo.middlewares.WeiboMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'WeiBo.pipelines.WeiboPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
SELENIUM_TIMEOUT = 20

PHANTOMJS_SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']

#MONGO_URI = 'localhost'
MONGO_URI = '10.170.130.140'

MONGO_DB = 'taobao'
