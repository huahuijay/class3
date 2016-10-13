# -*- coding: utf-8 -*-
import enums


def get_review_status_zh(transaction):
    if transaction.t_type == enums.TRANSACTION_LEAVE:
        if transaction.status == enums.TRANSACTION_STATUS_CREATE:
            return u'部门经理审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_MANAGER:
            return u'人事审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_HR:
            return u'人事经理审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_HR_MANAGER:
            return u'总经理审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_HR_MANAGER:
            return u'审核通过'

    elif transaction.t_type == enums.TRANSACTION_RAISE:
        if transaction.status == enums.TRANSACTION_STATUS_CREATE:
            return u'部门经理审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_MANAGER:
            return u'人事审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_HR:
            return u'人事经理审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_HR_MANAGER:
            return u'总经理审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_GM:
            if transaction.operate == enums.TRANSACTION_OPERATE_STATUS_CHECK:
                return u'人事处理中'
            elif transaction.operate == enums.TRANSACTION_OPERATE_STATUS_HR:
                return u'财务处理中'
            elif transaction.operate == enums.TRANSACTION_OPERATE_STATUS_ACCOUNT:
                return u'成功处理'

    elif transaction.t_type == enums.TRANSACTION_REIMBURSE:
        if transaction.status == enums.TRANSACTION_STATUS_CREATE:
            return u'部门经理审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_MANAGER:
            return u'财务审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_ACCOUNT:
            return u'财务经理审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_ACCOUNT_MANAGER:
            return u'总经理审核中'
        elif transaction.status == enums.TRANSACTION_STATUS_GM:
            if transaction.operate == enums.TRANSACTION_OPERATE_STATUS_CHECK:
                return u'财务处理中'
            elif transaction.operate == enums.TRANSACTION_OPERATE_STATUS_ACCOUNT:
                return u'成功处理'
