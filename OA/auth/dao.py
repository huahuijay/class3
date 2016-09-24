from models import Stuff


def create_stuff(name, password, sex, age):
    stuff = Stuff(name=name, password=password, sex=sex, age=age)
    stuff.save()

    return stuff
