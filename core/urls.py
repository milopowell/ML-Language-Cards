from django.urls import path
from .views import scenario_list_view, scenario_detail_view

urlpatterns = [
    path('', scenario_list_view, name='scenario_list'),
    path('<slug:slug>/', scenario_detail_view, name='scenario_detail'),
]