# -*- coding: utf-8 -*-
import mongoengine
from datetime import datetime
from busi import enums


class Transaction(mongoengine.Document):
    t_type = mongoengine.StringField(choices=enums.TRANSACTION_LIST)
    apply_time = mongoengine.DateTimeField(default=datetime.now)
