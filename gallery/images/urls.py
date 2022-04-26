from django.urls import path
from . import views

urlpatterns = [
    path('', views.hub, name = 'hub'),
    path('register/', views.registerUsers, name='register'),
    path('login/', views.loginUsers, name='login'),
    path('logout/', views.logoutUsers, name='logout'),
    path('image/<str:primary>/', views.view_image, name = 'view'),
    path('upload/', views.upload_image, name = 'upload'),
]