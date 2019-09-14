from django.conf.urls import url

from assignment import views

urlpatterns = [
    url(r'^assignment/$', views.assignQ, name='assignQ'),
    url(r'^assignment/inbox/(?P<id>\d+)/$', views.assignview, name='view'),
    url(r'^assignment/compose/$', views.compose, name='compose'),
    url(r'^assignment/sent/$', views.sent, name='sent'),
    url(r'^assignment/sent/(?P<id>\d+)/$', views.sentview, name='sentview'),
]