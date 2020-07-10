from django.urls import path
from . import views
urlpatterns =[
     path('',views.aboutme),
     path('contact',views.contact),
      path('about',views.about)
 ]