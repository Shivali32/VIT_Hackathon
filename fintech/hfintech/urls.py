from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('',views.index),
    
    path('login/',views.login),
    re_path('register/',views.register),
    path('404/',views.index),
    path('dashboard/',views.index),

]
