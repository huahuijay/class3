# -*- coding: utf-8 -*-
from base import BaseHandler
import dao


class LoginHandler(BaseHandler):
    def get(self):
        self.render('auth/login.html')


class RegisterHandler(BaseHandler):
    def get(self):
        self.render('auth/register.html')

    def post(self):
        username = self.get_argument('username', '')
        password1 = self.get_argument('password1', '')
        password2 = self.get_argument('password2', '')
        sex = self.get_argument('sex', '')
        age = self.get_argument('age', '')

        print type(sex)
        print type(username)

        if not (username and password1 and password2 and sex and age):
            self.write('lack of args')
            return

        if password1 != password2:
            self.write(u'两次密码输入不匹配')
            return

        sex = 1 if sex == 'male' else 2
        dao.create_stuff(username, password1, sex, int(age))
        self.write('register success')
