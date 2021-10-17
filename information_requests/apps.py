from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class InformationRequestsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "information_requests"
    verbose_name = "Pedidos de informação e denúncias"


class PrivateAdminConfig(AdminConfig):
    default_site = "information_requests.admin.PrivateAdminSite"
