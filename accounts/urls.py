from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("delete", views.delete, name="delete"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name='register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),


]