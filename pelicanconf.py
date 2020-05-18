#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bruffy53'
SITENAME = 'Linux and Python Snippets'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Brisbane'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Ars Technica', 'https://arstechnica.com/'),
     ('Wikipedia', 'https://wikipedia.org'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/mbdevaney'),
         ('Github', 'https://github.com/yourekittenme'),)

DEFAULT_PAGINATION = False

ARTICLE_PATHS = ['articles']

OUTPUT_PATH = '../output'
THEME = 'theme'

STATIC_PATHS = ['images', 'pdf']
PAGE_PATHS = ['pages']

PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites', ]

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

PYGMENTS_STYLE = 'monokai'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True