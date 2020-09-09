from .import views
from django.urls import path
from chart.views import (
    HomeView,
    ChartData
)
#app_name='chart'
urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('get_data/', views.get_data, name="api-data"),
    path('get_data/chart/', ChartData.as_view())#no need name option
]