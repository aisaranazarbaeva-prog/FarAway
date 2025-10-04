from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.tickets_list, name='list'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
