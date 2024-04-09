from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.create_user),
    path('update-password/<int:pk>', views.update_password),
    path('login/', views.user_login)
]