#Finsys Final
from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [

    path('',views.rodon_index,name='rodon_index'),
     path('home',views.home,name='home'),
      path('about',views.about,name='about'),
      path('contact',views.contact,name='contact'),



      path('login',views.login,name='login'),
       path('sendmessage',views.sendmessage,name='sendmessage'),
          path('logindata',views.logindata,name='logindata'),

      
]