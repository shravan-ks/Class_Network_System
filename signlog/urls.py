from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls) ),
    url(r'^', include('core.urls')),
    url(r'^', include('student.urls')),
    url(r'^', include('chat.urls', namespace="chat")),
    url(r'^', include('assignment.urls')),
    # url(r'^', include('feeds.urls')),
    url('^', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)