from django.urls import path 
from django.contrib.auth import views as auth_views
from . views import DashboardView

urlpatterns = [
    # user urls
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='accounts_login',
    ),

    # dashboard
    path('dashboard/', DashboardView.as_view(), name='accounts_dashboard'), 
]

"""
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""
