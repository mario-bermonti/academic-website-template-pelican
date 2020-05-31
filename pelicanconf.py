#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#######################################
# Customize your info
#######################################

# General settings
AUTHOR = "Academic Scholar"
SITENAME = "Academic Website"
SITEURL = ""
EMAIL = ""
TIMEZONE = ""
DEFAULT_LANG = "en"

# Appearance
# Theme
THEME = "themes/blueidea"

# ####################
# # Blogroll         #
# ####################
# # TODO: Add your links
# # To activate, uncomment the links tuple
# # To eliminate the ones you don't use, delete the whole line
# # To add new ones, copy/paste one and add the info
# LINKS = (
#     ("Pelican", "http://getpelican.com/"),
#     ("Python", "http://python.org/"),
#     ("You can modify those links in your config file", "#"),
# )

####################
# Social widget    #
####################
# TODO: Add links to your social networks
# To eliminate the ones you don't use, delete the whole line
# To add new ones, copy/paste one and add the info
SOCIAL = (
    ("ResearchGate", "#"),
    ("LinkedIn", "#"),
    ("ORCID", "#"),
    ("Google Scholar", "#"),
    ("Github", "#"),
    ("You can modify those links in your config file", "#"),
)

#################################################
# Don't modify unless you know what you are doing
#################################################

PATH = "content"
PAGE_ORDER_BY = "order"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
