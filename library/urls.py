from django.contrib import admin
from django.urls import path, include

from django.views.static import serve
from django.conf.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    repath(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    repath(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
