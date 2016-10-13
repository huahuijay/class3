from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def __initalize__(self):
        pass

    def get_current_user(self):
        user = self.get_secure_cookie('user')
        return user
