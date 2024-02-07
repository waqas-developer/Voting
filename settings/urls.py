from django.contrib import admin
from django.urls import path
from votingBooth.views import GetSlip
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", GetSlip.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
