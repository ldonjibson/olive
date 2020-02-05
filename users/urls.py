"""olive_app URL Configuration
"""
from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


from users.views import signup,ProfilePage,activate,change_password,DashBoardPage,MembersList,DashBoardRedirect

app_name='users'
urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name= 'users/login.html'), name='user_login'),
  path('logout/', auth_views.LogoutView.as_view(template_name= 'users/logged_out.html'), name='user_logout'),
  path('signup/', signup, name='signup_user'),

  path('profile/<str:username>', ProfilePage, name='user_profile'),
  path('', DashBoardRedirect, name='dashboardredirect'),
  path('dashboard/', DashBoardPage, name='dashboard'),
  path('members/', MembersList, name='members'),

  path('activate/<uidb64>/<token>/activate', activate, name='activate'),
  path('activations_sent', TemplateView.as_view(template_name='users/account_activation_sent.html'), name='account_activation_sent'),

  path('change-password', change_password, name='change_password'),
  path('password_reset', auth_views.PasswordResetView.as_view(template_name= 'users/password_reset_form.html'), name='password_reset'),
  path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name= 'users/password_reset_done.html'), name='password_reset_done'),
  path('reset/<uidb64>/<token>/reset',auth_views.PasswordResetConfirmView.as_view(template_name= 'users/password_reset_confirm.html'), name='password_reset_confirm'),
  path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name= 'users/password_reset_complete.html'), name='password_reset_complete'),

]