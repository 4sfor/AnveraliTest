from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

from .views import *

urlpatterns = [
    path("login/", LoginUserView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path("registration/", register_user, name='registration'),
    path("", index, name='index'),
    path("profile-employer/", profile_employer, name='profile_employer'),
    path("profile-worker/", profile_worker, name='profile_worker'),
    path("exp-add/", exp_add, name='exp_add'),
    path('delete-exp/',delete_exp, name='delete_exp'),
    path('reset-password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


