# -*- coding: utf-8 -*- #
AUTHOR = 'lyncir'
SITENAME = "Lyncir's Blog"
SITEURL = 'https://lyncir.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# 主题
THEME = "./pelican-themes/basic"

# 日期格式
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# 静态文件
STATIC_PATHS = ['images', 'htmls']
ARTICLE_PATHS = ['blog']

OUTPUT_PATH = 'docs/'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']
