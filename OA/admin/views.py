# -*- coding: utf-8 -*-
from base import BaseHandler
from common.utils import md5
from auth import dao as auth_dao
import dao


class AdminLoginHandler(BaseHandler):
    def get(self):
        if self.get_secure_cookie('admin_user'):
            self.redirect('/admin')
            return

        self.render('admin/login.html')

    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')

        if not username or not password:
            self.write('username or password can not be empty')
            return

        admin_user = dao.get_admin_user_by_name(username)
        if admin_user and admin_user.password == md5(password):
            self.set_secure_cookie('admin_user', username)
            self.redirect('/admin/')
        else:
            self.write('username does not match password')


class AdminHandler(BaseHandler):
    def get(self):
        stuff_list = auth_dao.get_stuff_list()
        self.render('admin/index.html', stuff_list=stuff_list)


class AddStuffHandler(BaseHandler):
    def get(self):
        self.render('admin/add_stuff.html')


class AddDepartmentHandler(BaseHandler):
    def get(self):
        self.render('admin/add_department.html')

    def post(self):
        name = self.get_argument('name')
        summary = self.get_argument('summary')

        auth_dao.create_department(name, summary)
        self.redirect('/admin')
