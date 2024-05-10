from django.urls import path
from placecode.views.country import *
from placecode.views.state import *
from placecode.views.city import *
urlpatterns = [
    # path()
    path('countries/', country_list, name='country-list'),
    path('countries/<str:country_code>/', country_detail, name='country-detail'),
    path('states/', state_list, name='state-list'),
    path('states/<str:state_code>/', state_detail, name='state-detail'),
    path('cities/', city_list, name='city-list'),
    path('cities/<str:country_code>/<str:state_code>/<str:city_code>/', city_detail, name='city-detail'),
]