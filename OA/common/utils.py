# -*- coding: utf-8 -*-

import hashlib
from mongoengine import connect
from settings import DB_HOST, DB_PORT, DB_NAME


def connect_db():
    connect(DB_NAME, host=DB_HOST, port=DB_PORT)


def md5(aString):
    return hashlib.md5(aString).hexdigest()
