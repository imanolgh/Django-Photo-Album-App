from django.urls import path
from . import views

urlpatterns = [
    path('', views.hub, name = 'hub'),
    path('image/<str:primary>/', views.view_image, name = 'view'),
    path('upload/', views.upload_image, name = 'upload'),
]