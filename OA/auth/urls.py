# -*- coding: utf-8 -*-
from auth import views


urlpatterns = [
    (r"/auth/login/?", views.LoginHandler),
    (r"/auth/register/?", views.RegisterHandler),
    (r"/auth/myevent/?", views.MyEventHandler),
    (r"/auth/create_event/?", views.CreateEventHandler),
]
