from django.urls import path
from django.contrib.auth import views as authviews

from . import views as userviews


urlpatterns = [
    path('reg/', userviews.register, name="reg"),
    path('auth/', authviews.LoginView.as_view(template_name='users/auth.html'), name="auth"),  # standard page of authorization. in template we write a file that would be reflect that finction
    path('exit/', authviews.LogoutView.as_view(template_name='users/exit.html'), name="exit"),  # standard page for out from authorization
    path('profile/', userviews.profile, name="profile"),
    path('password-reset/',
         authviews.PasswordResetView.as_view(template_name='users/pass_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         authviews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         authviews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         authviews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]