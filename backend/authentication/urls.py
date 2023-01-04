from django.urls import path
from . import views



urlpatterns=[
    path('login/',views.loginPage,name='login'),
    path('doLogin/',views.doLogin,name="doLogin"),
    path('logout/',views.logoutPage,name="logout")

]