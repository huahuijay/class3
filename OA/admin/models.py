# -*- coding: utf-8 -*-


import mongoengine


class AdminUser(mongoengine.Document):
    name = mongoengine.StringField()
    password = mongoengine.StringField()
