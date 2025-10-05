# tickets/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.tickets_list, name='tickets_list'),   # <-- важно: name='tickets_list'
    path('login/', auth_views.LoginView.as_view(template_name='tickets/login.html'), name='login'),
    path('signup/', views.signup_view, name='signup'),   # если у тебя есть кастомный view для регистрации
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
