from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'), 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
