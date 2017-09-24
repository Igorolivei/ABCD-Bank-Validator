#!/usr/bin/env python
import os

from waitress import serve
from pyramid.settings import asbool
import card_validator


# server info
host = '0.0.0.0'
port = int(os.environ.get('PORT', '8080'))

settings = {}
settings['pyramid.includes'] = ['pyramid_tm']
# debug mode
if asbool(os.environ.get('DEBUG', 0)):
    settings['pyramid.reload_templates'] = True
    settings['pyramid.debug_templates'] = True
    settings['pyramid.includes'].append('pyramid_debugtoolbar')

serve(card_validator.main({}, **settings), host=host, port=port)