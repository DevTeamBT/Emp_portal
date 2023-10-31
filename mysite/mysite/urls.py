from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.login, name='login'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('timesheet/', views.timesheet, name='timesheet'),
    path('sales/', views.sales, name='sales'),
    path('reqcan/', views.reqcan, name='reqcan'),
]
