# -*- coding: utf-8 -*-

from mongoengine import connect
from settings import DB_HOST, DB_PORT, DB_NAME


def connect_db():
    connect(DB_NAME, host=DB_HOST, port=DB_PORT)
