from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('main.urls', namespace='main')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
]
