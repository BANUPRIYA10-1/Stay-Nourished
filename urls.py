from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("", views.first, name='firsts'),
    path("logins", views.login, name='login'),
    path("registers",views.register,name='register'),
    path("home",views.home1,name='home'),
    path("about",views.about,name='about'),
    path("typesofdiet",views.typesofdiet,name='typesofdiet'),
    path("tellusaboutyou1",views.tellusaboutyou1,name='tellusaboutyou1'),
    path("tellusaboutyou",views.tellusaboutyou,name='tellusaboutyou'),
    path("logout",views.logout,name='logout'),
    path("knowyourfoods",views.knowyourfoods,name='knowyourfoods'),
    path("contactus",views.contactus,name='contactus'),
    path("gallery",views.gallery,name='gallery'),

]

