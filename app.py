# -*- coding: utf-8 -*-

"""
* Copyright (C) 2016 GridSafe, Inc.
"""
from collections import OrderedDict

from flask import Flask

from werkzeug.wsgi import DispatcherMiddleware, SharedDataMiddleware

f