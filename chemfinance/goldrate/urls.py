from django.urls import path
from .views import goldrate

urlpatterns = [
    path('goldrate/', goldrate, name='goldrate'),
]
