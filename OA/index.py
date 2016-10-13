from base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        user = self.get_current_user()
        data = locals()
        data.pop('self')

        print data
        self.render('index.html', **data)
