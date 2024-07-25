#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Generelle Blogeinstellungen
AUTHOR = u'Jan H. Krueger'
SITENAME = u'JHK Blog'
SITEURL = 'https://janhkrueger.github.io/'
SITESUBTITLE = 'Das private Blog von Jan H. Krueger'
TIMEZONE = 'Europe/Berlin'

DEFAULT_CATEGORY = 'Allgemein'
USE_FOLDER_AS_CATEGORY=True

PATH = 'content'
OUTPUT_PATH = 'public'

# global metadata to all the contents
DEFAULT_METADATA = (('jhk', 'blog'),)

STATIC_PATHS = ['extras/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': '/robots.txt'}
}

DEFAULT_LANG = u'de'
LOCALE = ('de_DE.utf8')
SLUGIFY_SOURCE = 'basename'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


THEME = '../pelican-bootstrap3'
TAG_CLOUD_MAX_ITEMS = 20
PYGMENTS_STYLE = 'friendly'
SHOW_ARTICLE_AUTHOR = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True


# Plugin Verwaltung
PLUGIN_PATHS = ['/data/pelican-plugins']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['/data/pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'code_include', 'global_license', 'gallery', 'i18n_subsites', 'series']


# Blogroll, Links im Seitenmenue
LINKS=(
    ('Piratenpartei','https://piratenpartei.de'),
    ('Free Software Foundation Europe','https://fsfe.org'),
    ('The game with no name','https://tgwnn.rpgame.de/'),
    ('Quest of Islands', 'https://www.questofislands.com/'),)

# Social widget
# Nur ein direkter Zugriff auf die RSS-Feeds
SOCIAL = (
    ('github', 'https://github.com/janhkrueger'),)


DEFAULT_PAGINATION = 5

# Lizenz unter welcher das Blog betrieben wird
CC_LICENSE = 'CC-BY-NC-SA'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Verhalten von Pages
WITH_FUTURE_DATES = True
ABOUT_ME = 'Software Architect. Gamer. Developer of Insulae. Traveler. C++ enthusiast. Pirate.'
