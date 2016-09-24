# -*- coding: utf-8 -*-
import os

PORT = 8000

DB_HOST = '127.0.0.1'
DB_PORT = 27017
DB_NAME = 'oa'


if PORT == 8000:
    DEBUG = True

settings = {
    'template_path': os.path.join(os.path.abspath('.'), 'templates'),
    'login_url': '/login/',
    'cookie_secret': '71ce02d856e6ee36dd6ca75696257f03',
    'xsrf_cookies': True,
    'static_path': os.path.join(os.path.abspath('.'), 'static'),
    'debug': DEBUG
}
