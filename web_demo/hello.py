# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.web import authenticated


class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, exception=None, **kwargs):
        print '888888888888a'
        print status_code
        if status_code == 500:
            print '9999'
            self.write('888')


class ErrorHandler(BaseHandler):
    def get(self):
        int('aa')


class MainHandler(tornado.web.RequestHandler):
    """处理请求的类"""
    def initialize(self):
        print 'in initialize'

    def prepare(self):
        print 'in prepare'
        # self.finish('888')

    def get1(self):
        a = 'aaa'
        b = 'bbb'
        c = 'ccc'
        params = locals()
        params.pop('self')
        self.render('test.html', **params)

    def get(self):
        self.write('''<html><body><form action="/" enctype="multipart/form-data" method="post">
                   <input type="text" name="message">
                   <input type="file" name="aaa">
                   <input type="submit" value="Submit">
                   </form></body></html>''')

    def post(self):
        # print self.request.arguments
        # print self.request.headers
        # print self.request.path
        # message = self.get_argument('message')
        print self.request.files['aaa']
        for f in self.request.files['aaa']:
            print f['body']

        # print 'message:', message
        self.write('')


class StoryHandler(BaseHandler):
    def get(self, story_type, story_id):
        print story_type, story_id
        self.write('storty_type:%s, story_id:%s' % (story_type, story_id))
        return
        # int('a')
        if 1:    # 假定他没有登陆
            self.redirect('/')
            return
        self.write('story number is:%s' % story_id)

settings = {
    'template_path': '.',
    'login_url': '/login/',
    'cookie_secret': '71ce02d856e6ee36dd6ca75696257f03',
    'xsrf_cookies': True,
    'static_path': '.',
    'debug': True
}


class TempHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('block.html')


class OutputHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write('write')
        # self.finish('finish')

        # self.render('test.html', a=8)
        self.redirect('http://www.baidu.com')


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        # 校验用户名和密码
        username = self.get_argument('username')
        # self.set_cookie('user', username)
        self.set_secure_cookie('user', username)

        next_url = self.get_argument('next', '')
        print 'next_url:', next_url
        if next_url:
            self.redirect(next_url)
        else:
            self.write('welcome, %s' % username)


class FastHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('fast')


class Slow1Handler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = AsyncHTTPClient()
        http.fetch('http://192.168.1.189:8001/third/', callback=self.on_response)
        self.write('slow')

    def on_response(self, response):
        self.finish('success')


class SlowHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        http = AsyncHTTPClient()
        response = yield http.fetch('http://192.168.1.189:8001/third/')
        print response
        self.write('slow')


class TestHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        print self.request.headers
        print self.request.arguments
        # user = self.get_cookie('user')
        user = self.get_secure_cookie('user')
        print 'get_secure_cookie:', user
        return user

    @authenticated
    def get(self):
        # user = self.get_current_user()
        # self.write('hello, %s' % user)
        b = ['aa', '<', 'cc', 'dd']
        self.render('test.html', a=2, b=b)


class XsrfHandler(tornado.web.RequestHandler):
    def post(self):
        self.write('111')

    # def check_xsrf_cookie(self):
    # return

    def get(self):
        self.render('xsrf.html')


app = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)/([0-9]+)", StoryHandler),
    (r"/output/?", OutputHandler),
    (r"/login/?", LoginHandler),
    (r"/test/?", TestHandler),
    (r"/error/?", ErrorHandler),
    (r"/xsrf/?", XsrfHandler),
    (r"/temp/?", TempHandler),
    (r"/fast/?", FastHandler),
    (r"/slow/?", SlowHandler),

], **settings)


if __name__ == '__main__':
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
