# -*- coding: utf-8 -*-
from auth import views


urlpatterns = [
    (r"/auth/login/?", views.LoginHandler),
    (r"/auth/register/?", views.RegisterHandler),
]
