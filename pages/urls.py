from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('industries/', views.industries, name='industries'),
    path('spx/', views.spx, name='spx')
]
