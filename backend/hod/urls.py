from . import views
from django.urls import path
app_name='hod'
urlpatterns=[
    path('dashboard/',views.dashboardPage,name="dashboard")
]