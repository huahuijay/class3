from models import Stuff, Department
from common.utils import md5


def create_stuff(name, password, sex, age):
    stuff = Stuff(name=name, password=md5(password), sex=sex, age=age)
    stuff.save()

    return stuff


def get_stuff_by_name(username):
    try:
        stuff = Stuff.objects.get(name=username)
    except:
        stuff = None

    return stuff


def get_stuff_list():
    stuff_list = Stuff.objects.all()

    return stuff_list


def create_department(name, summary):
    department = Department(name=name, summary=summary)
    department.save()

    return department
