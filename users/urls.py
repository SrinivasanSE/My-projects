from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name='users'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.CustomLoginView.as_view(),name='login'), #automatically renders registration/login.html page
    path('logout/',LogoutView.as_view(),name='logout'),  # automatically renders registration/logged_out.html page
    path('register/',views.register,name='register'),
    path('profile/', views.profile, name='profile'),
]

