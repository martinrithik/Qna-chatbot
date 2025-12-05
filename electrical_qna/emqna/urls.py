from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Main Q&A Platform Path
    path('', views.ask_question, name='ask_question'),
    
    # User Authentication Paths
    path('register/', views.register_user, name='register'),
    
    # Login Path (Uses Django's built-in view)
    path('login/', auth_views.LoginView.as_view(template_name='emqna/login.html'), name='login'),
    
    # Logout Path (Uses Django's built-in view)
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]