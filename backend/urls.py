from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flower/", include("flower.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

from . import views

app_name = "flower"

urlpatterns = [
    path("showall/", views.showall, name="showall"),
    path("upload/", views.upload, name="upload"),
    path("result/", views.result, name="result"),
]