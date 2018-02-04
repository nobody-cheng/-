from django.conf.urls import url
from . import views

urlpatterns = [
    # url('^', views.index),
    url('^index/', views.index),
    url('^get1/$', views.get1),
    url('^get2/$', views.get2),
    url('^get3/$', views.get3),
    url('^post1/$', views.post1),
    url('^post2/$', views.post2),
    url('^red1/$', views.red1),
    url('^json1/$', views.json1),
    url('^json2/$', views.json2),
    url('^cookie_set/$', views.cookie_set),
    url('^cookie_get/$', views.cookic_get),
    url('^session_test/$',views.session_test),
]