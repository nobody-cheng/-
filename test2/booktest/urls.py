from django.conf.urls import url
from .import views
urlpatterns=[
    # url('^$', views.index),
    url('^add/$', views.add),
    url('^delete(\d+)/$', views.delete),
    url('^area/$', views.area),
    url('^index/$', views.index),
    url('^verify_code/$', views.verify_code),
    url('^verify_show/$', views.verify_show)
]