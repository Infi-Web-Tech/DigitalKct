from . import views
from django.urls import path


urlpatterns=[
    path('dashboard',views.dashboardPage,name='dashboard')
]