from django.urls import path
from placecode.views.country import *
from placecode.views.state import *
from placecode.views.city import *
urlpatterns = [
    path('countries/', country_list, name='country-list'),
    path('countries/<str:country_code>/', country_update_delete, name='country-update-delete'),
    path('state/', state, name='state-list'),
    path('states/<str:country_code>/<str:state_code>/', state_update_delete, name='state-update-delete'),
    path('state-list/<str:country_code>/', state_list, name='state-list'),
    path('cities/', city, name='city-list'),
    path('cities/<str:country_code>/<str:state_code>/<str:city_code>/', city_update_delete, name='city-update-delete'),
    path('city-list/<str:country_code>/<str:state_code>/', city_list, name='city-list'),
]