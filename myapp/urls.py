from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='myapp-home'),
    path('my-home/', views.home, name='myapp-home-alias'),
    path('about/', views.about, name='myapp-about'),
]