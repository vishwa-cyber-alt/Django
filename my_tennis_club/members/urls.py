from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('form/', views.form, name='form'),
    path('signup/', views.signup, name='signup'),
    path('', views.homepage, name='homepage'),
    path('sum', views.sum, name='sum'),
]