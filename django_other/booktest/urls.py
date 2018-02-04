from django.conf.urls import url
from . import views

urlpatterns=[
    url('^index/$', views.index),
    url('^pic1/$', views.pic1),
    url('^pic2/$', views.pic2),
    url(r'^page(?P<pIndex>[0-9]*)/$', views.page_test),
]