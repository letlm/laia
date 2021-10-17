from django.urls import path

from information_requests.admin import admin_site, public_admin

urlpatterns = [
    path("admin/", admin_site.urls),
    path("", public_admin.urls),
]
