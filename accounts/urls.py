from django.urls import path
from . import views


urlpatterns = [
    # from the index page in listings
    path('login', views.login, name='login'),
    # listings/23(23 is the id)
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
