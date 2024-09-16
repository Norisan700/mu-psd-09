from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flower/", include("mu-psd-09.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

from . import server

app_name = "flower"

urlpatterns = [
    path("showall/", server.showall, name="showall"),
    path("upload/", server.upload, name="upload"),
    path("result/", server.result, name="result"),
]