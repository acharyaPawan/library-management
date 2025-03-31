from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #Here next page is default to LOGIN_REDIRECT_PAGE, which i have set to /dashboard
    path('signup/', SignUpView.as_view(), name='signup'), 
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),this is removed in django 5.0
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
