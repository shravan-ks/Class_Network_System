from django.conf.urls import url
from django.contrib.auth import views as auth_views
from core import views as core_views

app_name = 'core'

urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url(r'^base/$', core_views.base, name='base'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^Home/$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'},  name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'core:index'}, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]