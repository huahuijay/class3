# -*- coding: utf-8 -*-
import mongoengine
from datetime import datetime
from busi import enums


class Transaction(mongoengine.Document):
    stuff_id = mongoengine.StringField()
    t_type = mongoengine.IntField(choices=enums.TRANSACTION_LIST)
    content = mongoengine.StringField()
    apply_time = mongoengine.DateTimeField(default=datetime.now)
    status = mongoengine.IntField(choices=enums.TRANSACTION_STATUS_LIST, default=enums.TRANSACTION_STATUS_CREATE)
    operate = mongoengine.IntField(choices=enums.TRANSACTION_OPERATE_STATUS_LIST, default=enums.TRANSACTION_OPERATE_STATUS_CHECK)
