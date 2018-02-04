from django.conf.urls import url
from .import views

urlpatterns = [
    url('^$', views.index),
    url('^book/$', views.book),
    url(r'^hero(\d+)', views.hero),
]

