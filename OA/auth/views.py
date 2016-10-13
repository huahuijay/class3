# -*- coding: utf-8 -*-
from base import BaseHandler
from common.utils import md5
from tornado.web import authenticated
import dao
from busi import enums as busi_enums
from busi import dao as busi_dao
from busi import utils as busi_utils


class LoginHandler(BaseHandler):
    def get(self):
        self.render('auth/login.html')

    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')

        if not username or not password:
            self.write('username or password can not be empty')
            return

        stuff = dao.get_stuff_by_name(username)
        if stuff and stuff.password == md5(password):
            self.set_secure_cookie('user', username)
            self.redirect('/')
        else:
            self.write('username does not match password')


class RegisterHandler(BaseHandler):
    def get(self):
        self.render('auth/register.html')

    def post(self):
        username = self.get_argument('username', '')
        password1 = self.get_argument('password1', '')
        password2 = self.get_argument('password2', '')
        sex = self.get_argument('sex', '')
        age = self.get_argument('age', '')

        if not (username and password1 and password2 and sex and age):
            self.write('lack of args')
            return

        if password1 != password2:
            self.write(u'两次密码输入不匹配')
            return

        sex = 1 if sex == 'male' else 2
        dao.create_stuff(username, password1, sex, int(age))
        self.write('register success')


class MyEventHandler(BaseHandler):
    @authenticated
    def get(self):
        user = self.get_current_user()
        stuff = dao.get_stuff_by_name(user)

        transaction_list = busi_dao.get_transaction_list(stuff_id=str(stuff.id))
        result = []
        for transaction in transaction_list:
            print transaction.to_json()
            result.append([transaction.content, busi_utils.get_review_status_zh(transaction)])
        self.render('auth/myevent.html', transaction_list=result)


class CreateEventHandler(BaseHandler):
    @authenticated
    def get(self):
        t_type_list = busi_enums.TRANSACTION_LIST

        self.render('auth/create_event.html', t_type_list=t_type_list, zh_t_type_dict=busi_enums.ZH_TTYPE_DICT)

    @authenticated
    def post(self):
        t_type = self.get_argument('t_type', '')
        content = self.get_argument('content', '')

        if not content:
            self.write('content can not be empty')

        print 'creat event:', t_type, content
        user = self.get_current_user()
        stuff = dao.get_stuff_by_name(user)
        busi_dao.create_transaction(t_type, content, stuff_id=str(stuff.id))
        self.redirect('/auth/myevent')
