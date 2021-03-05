from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('biblio/', include('biblio.urls')),
    path('admin/', admin.site.urls),
]
