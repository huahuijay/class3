import auth.urls
import index


urlpatterns = [
    (r"/", index.IndexHandler),
]


urlpatterns += auth.urls.urlpatterns
