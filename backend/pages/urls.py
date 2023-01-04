from django.urls  import path
from . import views

urlpatterns=[
                path('',views.homepage,name="homepage"),
                path('contact',views.contactpage,name="contact"),
                path('services',views.servicespage,name="services"),
                path('about/',views.aboutpage,name='services'),
                path('explore/',views.explorepage,name='explore'),
                
]