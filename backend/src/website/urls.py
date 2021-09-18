from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api", include("api.urls")),
    path("account/", include("account.urls")),
    path("order/", include("order.urls")),
]
