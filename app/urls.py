from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login1,name='login'),
    path('profile/',views.profile,name='profile'),
    path('search/',views.search_bar,name='search'),
]
