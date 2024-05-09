from django.urls import path
from user.views import user, loginlogout

urlpatterns = [
    path('create-user/', user.user),
    path('update-password/', user.change_password),
    path('login/', loginlogout.user_login),
    path('logout/', loginlogout.logout),
]