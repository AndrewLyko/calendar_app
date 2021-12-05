from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('details', views.details, name="details"),
]
