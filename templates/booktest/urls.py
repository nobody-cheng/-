from django.conf.urls import url
from . import  views
urlpatterns = [
    url('^index/', views.index),
    url(r'^bianliang/$', views.bianliang),
    url(r'^biaoqian/$', views.biaoqian),
    url('^glq/$', views.glq),
    url('^list/$', views.list),
    url('^zhuanyi/$', views.zhuanyi),
    url('^verify_code/$',views.verify_code),
    url('^yzm1/$', views.yzm1),
    url('^yzm2/$', views.yzm2),
]