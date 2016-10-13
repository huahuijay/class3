# -*- coding: utf-8 -*-
from admin import views


urlpatterns = [
    (r"/admin/?", views.AdminHandler),
    (r"/admin/login/?", views.AdminLoginHandler),
    (r"/admin/add_stuff/?", views.AddStuffHandler),
    (r"/admin/add_department/?", views.AddDepartmentHandler),
]
