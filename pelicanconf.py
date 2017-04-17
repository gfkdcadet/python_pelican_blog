#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Cronin'
SITENAME = "Chris' Blog"
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = 'MBA & Data Scientist'
SITELOGO = SITEURL + '/images/profshot.jpg'
FAVICON = SITEURL + '/images/dodgest_logo3.jpg'

#THEME = '/Users/Cronin/pelican-themes/Flex-master'
THEME = 'Flex-master'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

MENUITEMS = (('Projects','/category/projects.html'),
             ('Tags', '/tags.html'),
             ('Resources','/pages/resources.html'),)

# Blogroll
LINKS = (('About','/pages/about.html'),
        ('Projects','/category/projects.html'),
        ('Programs','/pages/programs.html'),
        ('Conferences','/pages/conferences.html'),)

# Social widget
SOCIAL = (('linkedin',  'https://www.linkedin.com/in/cvcronin'),
          ('github', 'https://github.com/ccronin51'),)
          #('dribbble', 'http://www.dodgestreetventures.com'))


DEFAULT_PAGINATION = 11

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Enable Jinja2 i18n extension used to parse translations.
#JINJA_ENVIRONMENT = ['jinja2.ext.i18n']

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
