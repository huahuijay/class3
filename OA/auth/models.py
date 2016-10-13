# -*- coding: utf-8 -*-


import mongoengine
from auth import enums
from datetime import datetime


class Department(mongoengine.Document):
    name = mongoengine.StringField()


class Stuff(mongoengine.Document):
    name = mongoengine.StringField()
    sex = mongoengine.IntField()
    age = mongoengine.IntField()
    department_id = mongoengine.StringField()
    position = mongoengine.IntField(choices=enums.STUFF_LIST)   # 职位
    entry_time = mongoengine.DateTimeField(default=datetime.now)   # 入职时间
    password = mongoengine.StringField()
