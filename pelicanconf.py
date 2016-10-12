#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Eric Yang'
SITENAME = 'Big Data Insight'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'bootstrap2'
DISQUS_SITENAME = 'bigdatainsight'
GOOGLE_ANALYTICS = 'UA-85530588-1'
USE_FOLDER_AS_CATEGORY = True
MENUITEMS = (("GITHUB","http://github.com"),
             ("SEARCH","http://google.com"))

#加载plugins
PLUGIN_PATHS = ["pelican-plugins"]
MARKUP = ('md', 'pelican-ipynb')
PLUGINS = ["sitemap", "pelican-ipynb.markup"]

#相关文章
RELATED_POSTS_MAX = 10

#sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}
