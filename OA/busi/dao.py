from busi import models


def create_transaction(t_type, content, stuff_id):
    t = models.Transaction(t_type=t_type, content=content, stuff_id=stuff_id)
    t.save()

    return t


def get_transaction_list(**kwargs):
    print kwargs
    transaction_list = models.Transaction.objects.filter(**kwargs)
    return transaction_list
