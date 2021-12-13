from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from web import urls as web_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(web_urls)),
]
