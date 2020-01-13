from django.urls import path

from . import views

urlpatterns = [
  path('', views.hello, name='hello'),
  path('get/', views.get, name='get'),
  path('post/', views.post, name='post'),
]