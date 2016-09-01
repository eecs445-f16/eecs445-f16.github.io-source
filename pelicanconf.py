#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals;
import datetime;

# No Cache
LOAD_CONTENT_CACHE = False;

# Site Information
AUTHOR = 'EECS 445 Course Staff';
SITENAME = 'eecs445-f16';
SITEURL = '';
TIMEZONE = 'America/Detroit';
DEFAULT_LANG = 'en';

# Basic Settings
PATH = 'content'

# Custom Settings (custom variables defined by me, for use by templates)
SITE_LAST_MODIFIED = SITE_LAST_MODIFIED = datetime.datetime.now();

## Pages, Paths, and URLs ------------------------------------------------------


## Content Generation ----------------------------------------------------------

# Delete output directory when regenerating, but save Git repositories.
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git", ".gitignore", ".git/*"]

## External Links / Plugins ----------------------------------------------------

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

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
