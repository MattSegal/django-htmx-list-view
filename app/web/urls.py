from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.list_view, name="list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
