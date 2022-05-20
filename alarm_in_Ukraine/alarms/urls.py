from django.urls import path
from . import views


urlpatterns = [
    path('', views.Statistic.as_view(), name='all_statistic'),
    path('week_statistic/', views.StatisticWeek.as_view(), name='week_statistic'),
    path('today_statistic/', views.StatisticDay.as_view(), name='today_statistic'),
]