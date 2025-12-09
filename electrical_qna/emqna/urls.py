from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.ask_question, name='ask_question'),

    path('register/', views.register_user, name='register'),
    
   
    path('login/', auth_views.LoginView.as_view(template_name='emqna/login.html'), name='login'),
    
 
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]