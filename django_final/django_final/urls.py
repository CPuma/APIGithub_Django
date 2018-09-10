
from django.contrib import admin
from django.urls import path, include
from core.views import search
from core.urls import core_patterns

urlpatterns = [
    path('', include(core_patterns)),
    path('admin/', admin.site.urls),
]
