from django.urls import path
from admin_material import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name="index"),
    path('tables/', views.tables, name="tables"),
    path('billing/', views.billing, name="billing"),
    path('virtual-reality/', views.virtual_reality, name="virtual_reality"),
    path('rtl/', views.rtl, name="rtl"),
    path('notifications/', views.notifications, name="notifications"),
    path('profile/', views.profile, name="profile"),
    path('map/', views.map, name="map"),
    path('icons/', views.icons, name="icons"),
    path('typography/', views.typography, name="typography"),
    path('template/', views.template, name="template"),

    # Authentication
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='pages/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='pages/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='pages/password_reset_complete.html'
    ), name='password_reset_complete'),
]