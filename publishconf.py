#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals;

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os;
import sys;
sys.path.append(os.curdir);
from pelicanconf import *;

SITEURL = 'http://eecs445-f16.github.io';
RELATIVE_URLS = False;

## Plugins ---------------------------------------------------------------------

# Disqus Comments
DISQUS_SITENAME = "benrbray";

# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml';
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml';
