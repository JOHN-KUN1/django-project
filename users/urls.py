from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('register/',views.register_page),
    path('login/', views.login_page, name='loginPage'),
    path('logout/',views.logout_page, name='logout')
]